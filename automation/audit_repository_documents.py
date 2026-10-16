#!/usr/bin/env python3
"""Read-only static audit for the CONSORCIO governance workflow."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

CONTROL = {"SHA-256 (conteúdo canónico)", "Commit de referência (versão anterior)"}
REQUIRED = {"ID", "Projeto", "Repositório", "Tipo documental", "Fase", "Estado", "Versão", "SHA-256 (conteúdo canónico)", "Commit de referência (versão anterior)", "Data de criação", "Data de atualização", "Responsável", "Aprovador", "Origem", "Autoridade superior", "Cadeia de autoridade"}
STATES = {"RASCUNHO", "EM_REVISAO", "APROVADO", "DEPRECADO", "REJEITADO", "PROPOSTO", "EM_CURSO", "BLOQUEADO", "CONCLUIDO", "APROVACAO_CONDICIONAL_REGISTADA"}
ID_RE = re.compile(r"^[A-Z0-9À-Þ]+(?:-[A-Z0-9À-Þ]+)*$")
HASH_RE = re.compile(r"^[0-9a-f]{64}$")
SKIP = {".git", ".governanca-master", "node_modules", ".venv", "venv", "__pycache__", "site-packages", "dados", "data", "vendor", "build", "dist"}

def canonical(text):
    text = text.removeprefix("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    result = []
    for line in text.splitlines(keepends=True):
        m = re.match(r"^\|\s*\*\*(.*?)\*\*\s*\|", line)
        if not (m and m.group(1).strip() in CONTROL): result.append(line)
    return "".join(result).encode("utf-8")

def parse(text):
    problems=[]; text=text.removeprefix("\ufeff").replace("\r\n","\n").replace("\r","\n"); lines=text.splitlines()
    if not lines or not lines[0].startswith("# "): return {}, ["Ficheiro não começa com título H1."]
    if len(lines)<5 or lines[2].strip()!="| Campo | Valor |" or lines[3].replace(" ","")!="|---|---|": return {}, ["Cabeçalho não contém tabela Markdown canónica nas primeiras linhas."]
    fields={}
    for line in lines[4:]:
        if not line.strip().startswith("|"): break
        parts=[x.strip() for x in line.strip().strip("|").split("|",1)]
        if len(parts)!=2: problems.append("Linha de metadados inválida."); continue
        key=re.sub(r"^\*\*(.*?)\*\*$",r"\1",parts[0]).strip()
        if key in fields: problems.append("Campo duplicado: "+key)
        fields[key]=parts[1]
    missing=sorted(REQUIRED-fields.keys())
    if missing: problems.append("Campos obrigatórios ausentes: "+", ".join(missing))
    return fields,problems

def audit(path,root):
    rel=path.relative_to(root).as_posix(); warns=[]; fails=[]
    try: text=path.read_bytes().decode("utf-8")
    except (OSError,UnicodeDecodeError) as e: return {"path":rel,"status":"FAIL","failures":["Leitura UTF-8 falhou: "+str(e)],"warnings":[]}
    fields,problems=parse(text); fails.extend(problems)
    actual=hashlib.sha256(canonical(text)).hexdigest()
    if fields:
        doc_id=fields.get("ID",""); state=fields.get("Estado",""); version=fields.get("Versão","")
        if not ID_RE.fullmatch(doc_id): fails.append("ID documental inválido.")
        if state not in STATES: warns.append("Estado fora do conjunto reconhecido: "+repr(state))
        if not re.fullmatch(r"\d+\.\d+\.\d+",version): warns.append("Versão não segue MAJOR.MINOR.PATCH.")
        for f in ("Data de criação","Data de atualização"):
            try: datetime.strptime(fields.get(f,""),"%Y-%m-%d")
            except ValueError: warns.append(f+" deve usar AAAA-MM-DD.")
        given=fields.get("SHA-256 (conteúdo canónico)","")
        if not HASH_RE.fullmatch(given): warns.append("SHA-256 canónico ausente ou placeholder.")
        elif given != actual: fails.append("SHA-256 canónico divergente; calculado="+actual)
        if state=="APROVADO" and (not fields.get("Aprovador") or "pendente" in fields.get("Aprovador","").lower()): fails.append("APROVADO sem aprovador identificável.")
        ref=fields.get("Commit de referência (versão anterior)","")
        if not ref or ref=="N/A": warns.append("Commit anterior não referenciado ou sem justificação.")
        elif "N/A" in ref and "documento inicial" not in ref.lower() and "relatório gerado" not in ref.lower(): warns.append("Exceção N/A para commit anterior carece de justificação.")
        if "PROMPTS" not in fields.get("Cadeia de autoridade","") or "CÓDIGO" not in fields.get("Cadeia de autoridade",""): warns.append("Cadeia de autoridade incompleta.")
        if not fields.get("Autoridade superior"): warns.append("Autoridade superior ausente.")
        if not fields.get("Origem"): warns.append("Origem ausente.")
        body_lines=text.replace("\r\n","\n").replace("\r","\n").splitlines()[1:]
        headings={line.strip() for line in body_lines if line.startswith("## ")}
        required_sections={"## Estado","## Evidências","## Validação","## Resultado","## Próxima Ação"}
        missing=sorted(required_sections-headings)
        if missing: warns.append("Secções não encontradas quando aplicáveis: "+", ".join(missing))
    status="FAIL" if fails else ("WARN" if warns else "PASS")
    return {"path":rel,"id":fields.get("ID",""),"title":(text.splitlines() or [""])[0],"declared_state":fields.get("Estado",""),"sha256_calculated":actual,"status":status,"failures":fails,"warnings":warns}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--repo-root",required=True,type=Path); p.add_argument("--governance-root",required=True,type=Path); p.add_argument("--report",required=True,type=Path); p.add_argument("--json",required=True,dest="json_path",type=Path); a=p.parse_args()
    root=a.repo_root.resolve(); gov=a.governance_root.resolve()
    if not root.is_dir() or not gov.is_dir(): print("Diretório do projeto ou governação não existe.",file=sys.stderr); return 2
    global_warnings=[]; constitution=gov/"CONSTITUICAO.md"; standard=gov/"CABEÇALHO"/"NORMA-CABECALHO-PADRAO.md"
    if not constitution.exists(): global_warnings.append("Constituição mestre não encontrada.")
    if not standard.exists(): global_warnings.append("Norma mestre de cabeçalho não encontrada.")
    else:
        mt=standard.read_text(encoding="utf-8")
        if "1.0.3" not in mt or "APROVADO" not in mt: global_warnings.append("Norma mestre mudou de versão/estado; requer revisão de impacto.")
    records=[]; ids={}; report_path=a.report.resolve(); json_path=a.json_path.resolve()
    for path in sorted(root.rglob("*.md")):
        rel=path.relative_to(root)
        if any(part in SKIP for part in rel.parts) or path.resolve() in {report_path,json_path}: continue
        rec=audit(path,root); records.append(rec)
        if rec.get("id"): ids.setdefault(rec["id"],[]).append(rec["path"])
    for doc_id,paths in ids.items():
        if len(paths)>1:
            for rec in records:
                if rec.get("id")==doc_id: rec["failures"].append("ID duplicado: "+", ".join(paths)); rec["status"]="FAIL"
    stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
    counts={s:sum(1 for x in records if x["status"]==s) for s in ("PASS","WARN","FAIL")}; status="FAIL" if counts["FAIL"] else ("WARN" if counts["WARN"] else "PASS")
    lines=["# Relatório diário de governação — CONSORCIO","","| Campo | Valor |","|---|---|","| **ID** | CONSORCIO-REL-GOV-DAILY-001 |","| **Projeto** | CONSORCIO |","| **Repositório** | [carlos-andrade/CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) |","| **Tipo documental** | RELATORIO |","| **Fase** | G1 — Inventário e auditoria |",f"| **Estado** | {status} |","| **Versão** | 1.0.0 |","| **SHA-256 (conteúdo canónico)** | GERADO_NO_RELATORIO_JSON |","| **Commit de referência (versão anterior)** | N/A — relatório gerado por execução diária |",f"| **Data de criação** | {stamp[:10]} |",f"| **Data de atualização** | {stamp[:10]} |","| **Responsável** | GitHub Actions |","| **Aprovador** | Não aplicável — evidência automática, não aprovação humana |","| **Origem** | Auditoria documental automatizada |","| **Autoridade superior** | [GOVERNANCA.md](../GOVERNANCA.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |","| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |","","## Estado","",f"Execução UTC: `{stamp}`. Ficheiros Markdown analisados: **{len(records)}**.","","| Resultado | Quantidade |","|---|---:|",f"| PASS | {counts['PASS']} |",f"| WARN | {counts['WARN']} |",f"| FAIL | {counts['FAIL']} |","","## Evidências","","O JSON da mesma execução contém resultados detalhados por ficheiro. A fonte normativa é a branch `main` corrente de GOVERNANCA.","","## Validação","","- Auditoria estática e de leitura; os documentos auditados não são reescritos.","- SHA-256: UTF-8/LF, sem BOM, excluindo somente as duas linhas de controlo.","- Não equivale a aprovação humana nem garante disponibilidade de ligações externas.","- A ausência de execução ou evidência nunca equivale a PASS.","","## Resultados por documento","","| Ficheiro | ID | Estado declarado | Resultado | Falhas | Avisos |","|---|---|---|---|---:|---:|"]
    for rec in records: lines.append(f"| `{rec['path']}` | {rec.get('id','')} | {rec.get('declared_state','')} | **{rec['status']}** | {len(rec['failures'])} | {len(rec['warnings'])} |")
    lines += ["","## Pendências globais",""] + (["- "+w for w in global_warnings] if global_warnings else ["- Nenhuma pendência global detetada."]) + ["","## Resultado","",f"Contagem: PASS={counts['PASS']}, WARN={counts['WARN']}, FAIL={counts['FAIL']}. O relatório não certifica conformidade global nem substitui gates G0–G6.","","## Próxima Ação","","Corrigir falhas em lotes controlados, preservar histórico, recalcular os hashes afetados e executar novamente o workflow.",""]
    a.report.parent.mkdir(parents=True,exist_ok=True); a.json_path.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text("\n".join(lines),encoding="utf-8",newline="\n")
    payload={"schema_version":1,"repository":"carlos-andrade/CONSORCIO","generated_at_utc":stamp,"governance_source":"https://github.com/carlos-andrade/GOVERNANCA/tree/main","master_constitution_exists":constitution.exists(),"records":records,"summary":counts,"global_warnings":global_warnings,"note":"Auditoria estática de leitura; não reescreve documentos."}
    a.json_path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"summary":counts,"report":str(a.report),"json":str(a.json_path)},ensure_ascii=False))
    return 1 if counts["FAIL"] else 0

if __name__=="__main__": raise SystemExit(main())
