import hashlib
import unittest

from automation.audit_repository_documents import canonical, parse, STATES

class GovernanceAuditTests(unittest.TestCase):
    def test_canonical_excludes_only_two_control_rows(self):
        text = '# Título\n\n| Campo | Valor |\n|---|---|\n| **ID** | TEST-001 |\n| **SHA-256 (conteúdo canónico)** | placeholder |\n| **Commit de referência (versão anterior)** | commit |\n\nCorpo\n'
        expected = text.replace('| **SHA-256 (conteúdo canónico)** | placeholder |\n', '').replace('| **Commit de referência (versão anterior)** | commit |\n', '')
        self.assertEqual(canonical(text), expected.encode('utf-8'))
        self.assertEqual(hashlib.sha256(canonical(text)).hexdigest(), hashlib.sha256(expected.encode('utf-8')).hexdigest())

    def test_conditional_approval_state_is_recognized(self):
        self.assertIn('APROVACAO_CONDICIONAL_REGISTADA', STATES)

    def test_parse_required_metadata(self):
        text = '\n'.join([
            '# Teste', '', '| Campo | Valor |', '|---|---|',
            '| **ID** | TEST-001 |', '| **Projeto** | Teste |',
            '| **Repositório** | [x](https://github.com/a/b) |',
            '| **Tipo documental** | TESTE |', '| **Fase** | G0 |',
            '| **Estado** | RASCUNHO |', '| **Versão** | 1.0.0 |',
            '| **SHA-256 (conteúdo canónico)** | ' + ('a' * 64) + ' |',
            '| **Commit de referência (versão anterior)** | N/A — documento inicial |',
            '| **Data de criação** | 2026-10-16 |', '| **Data de atualização** | 2026-10-16 |',
            '| **Responsável** | Equipa |', '| **Aprovador** | Pendente |',
            '| **Origem** | Teste |', '| **Autoridade superior** | Norma |',
            '| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |',
            '', '## Estado', 'ok',
        ])
        fields, errors = parse(text)
        self.assertEqual(fields['ID'], 'TEST-001')
        self.assertEqual(errors, [])

if __name__ == '__main__':
    unittest.main()
