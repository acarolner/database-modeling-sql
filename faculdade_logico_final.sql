-- 1) Criando banco
CREATE DATABASE IF NOT EXISTS faculdade_db_estudante
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE faculdade_db_estudante;

-- 2) Tabelas principais
-- 2.1) FACULDADE
CREATE TABLE faculdade (
id_faculdade INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(150) NOT NULL,
sigla VARCHAR(20) NOT NULL,
cnpj CHAR(14) NOT NULL,
endereco VARCHAR(200),
telefone VARCHAR(20),
email VARCHAR(120),
UNIQUE KEY uk_faculdade_sigla (sigla),
UNIQUE KEY uk_faculdade_cnpj (cnpj)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.2) DEPARTAMENTO  
CREATE TABLE departamento (
id_departamento INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(120) NOT NULL,
sigla VARCHAR(20) NOT NULL,
faculdade_id INT NOT NULL,
UNIQUE KEY uk_departamento_sigla_uni (sigla, faculdade_id),
CONSTRAINT fk_faculdade_universidade
FOREIGN KEY ( faculdade_id) REFERENCES  faculdade(id_faculdade)
ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.3) CURSO (pertence a uma universidade)
CREATE TABLE curso (
id_curso INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(120) NOT NULL,
grau VARCHAR(20) NOT NULL, -- TECNOLOGO | BACHAREL | LICENCIATURA
carga_horaria INT NOT NULL,
faculdade_id INT NOT NULL,
UNIQUE KEY uk_curso_nome_uni (nome, faculdade_id),
CONSTRAINT fk_curso_faculdade
FOREIGN KEY (faculdade_id) REFERENCES faculdade (id_faculdade)
ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.4) PROFESSOR 
CREATE TABLE professor (
id_professor INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(120) NOT NULL,
cpf CHAR(11) NOT NULL,
email VARCHAR(120) NOT NULL,
titulacao VARCHAR(20) NOT NULL, -- GRADUACAO | ESPECIALIZACAO | MESTRADO | DOUTORADO
departamento_id INT,
UNIQUE KEY uk_professor_cpf (cpf),
UNIQUE KEY uk_professor_email (email),
CONSTRAINT fk_prof_depart FOREIGN KEY (departamento_id)
REFERENCES departamento (id_departamento)
ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.5) ALUNO 
CREATE TABLE aluno (
id_aluno INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(120) NOT NULL,
cpf CHAR(11) NOT NULL,
email VARCHAR(120) NOT NULL,
data_nascimento DATE,
status VARCHAR(15) NOT NULL DEFAULT 'ATIVO', -- ATIVO | INATIVO
curso_id INT NULL,
UNIQUE KEY uk_aluno_cpf (cpf),
UNIQUE KEY uk_aluno_email (email),
CONSTRAINT fk_aluno_curso FOREIGN KEY (curso_id)
REFERENCES curso (id_curso)
ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.6) DISCIPLINA  
CREATE TABLE disciplina (
id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
codigo VARCHAR(20) NOT NULL,
nome VARCHAR(120) NOT NULL,
carga_horaria INT NOT NULL,
curso_id INT NOT NULL,
UNIQUE KEY uk_disciplina_codigo (codigo),
CONSTRAINT fk_disc_curso FOREIGN KEY (curso_id)
REFERENCES curso (id_curso)
ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.7) Pré-requisitos de DISCIPLINA (auto-relacionamento N:N)
CREATE TABLE disciplina_prereq (
disciplina_id INT NOT NULL,
prereq_id INT NOT NULL,
PRIMARY KEY (disciplina_id, prereq_id),
CONSTRAINT fk_pr_discip FOREIGN KEY (disciplina_id)
REFERENCES disciplina (id_disciplina)
ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT fk_pr_req FOREIGN KEY (prereq_id)
REFERENCES disciplina (id_disciplina)
ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.8) TURMA (oferta de uma disciplina em um semestre)
CREATE TABLE turma (
id_turma INT AUTO_INCREMENT PRIMARY KEY,
disciplina_id INT NOT NULL,
professor_id INT NOT NULL,
semestre VARCHAR(10) NOT NULL, -- ex.: 2025.1
turno VARCHAR(10) NOT NULL, -- MANHA | TARDE | NOITE
capacidade INT NOT NULL,
UNIQUE KEY uk_turma_oferta (disciplina_id, professor_id, semestre, turno),
CONSTRAINT fk_turma_disc FOREIGN KEY (disciplina_id)
REFERENCES disciplina (id_disciplina)
ON UPDATE CASCADE ON DELETE RESTRICT,
CONSTRAINT fk_turma_prof FOREIGN KEY (professor_id)
REFERENCES professor (id_professor)
ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.9) MATRÍCULA_TURMA (Aluno x Turma)
CREATE TABLE matricula_turma (
id_matricula INT AUTO_INCREMENT PRIMARY KEY,
aluno_id INT NOT NULL,
turma_id INT NOT NULL,
status VARCHAR(15) NOT NULL DEFAULT 'MATRICULADO', -- MATRICULADO | TRANCADO | APROVADO | REPROVADO
nota DECIMAL(4,2),
frequencia DECIMAL(5,2),
data_lancamento TIMESTAMP NULL DEFAULT NULL,
UNIQUE KEY uk_matricula_aluno_turma (aluno_id, turma_id),
CONSTRAINT fk_mat_aluno FOREIGN KEY (aluno_id)
REFERENCES aluno (id_aluno)
ON UPDATE CASCADE ON DELETE RESTRICT,
CONSTRAINT fk_mat_turma FOREIGN KEY (turma_id)
REFERENCES turma (id_turma)
ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

