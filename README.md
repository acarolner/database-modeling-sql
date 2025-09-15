from pathlib import Path

# 🎓 Sistema Acadêmico - Banco de Dados SQL

Este projeto implementa um **banco de dados relacional** para gerenciamento de uma faculdade, cobrindo desde a estrutura institucional até o controle acadêmico de alunos e turmas.

Projeto desenvolvido como *Portifólio* da disciplina de Banco de Dados Lógico (UNIFECAF).

---

## 👩💻 Autora
- **Anna Caroline Ribeiro**
- GitHub: [acarolner](https://github.com/acarolner)

---

## 📦 Estrutura do Banco de Dados

O script **faculdade_logico_final.sql** cria o banco de dados `faculdade_db_estudante` e suas tabelas principais:

1. **faculdade** → informações gerais da instituição.
2. **departamento** → departamentos acadêmicos vinculados à faculdade.
3. **curso** → cursos oferecidos (tecnólogo, bacharelado, licenciatura).
4. **professor** → dados de professores e vínculo com departamentos.
5. **aluno** → cadastro de estudantes e vínculo com cursos.
6. **disciplina** → catálogo de disciplinas de cada curso.
7. **disciplina_prereq** → pré-requisitos entre disciplinas.
8. **turma** → oferta de disciplinas em semestres/turnos com professor responsável.
9. **matricula_turma** → matrícula dos alunos em turmas, incluindo notas e frequência.

---

## 🔑 Regras e Restrições

- **Chaves primárias**: definidas em todas as tabelas.
- **Chaves estrangeiras**: garantem a integridade referencial entre faculdades, cursos, alunos, professores e disciplinas.
- **Constraints de unicidade**: como `cpf`, `email`, `sigla`, entre outros.
- **Auto-relacionamento**: tabela `disciplina_prereq` (pré-requisitos entre disciplinas).
- **Controle de matrículas**: tabela `matricula_turma` armazena status (matriculado, aprovado, reprovado).

---

## ▶️ Como usar

1. Certifique-se de ter o **MySQL** instalado.
2. Execute o script SQL no terminal ou em um cliente (como Workbench):

```bash
mysql -u root -p < faculdade_logico_final.sql
