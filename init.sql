CREATE DATABASE money_mastery;

\c money_mastery;

SET search_path TO public;

CREATE TYPE categoria AS ENUM ('LAZER', 'ALIMENTACAO', 'SAUDE', 'MORADIA',  'TRANSPORTE', 'EDUCACAO', 'OUTRO');
CREATE TYPE forma_pagamento AS ENUM ('CREDITO', 'DEBITO', 'PIX', 'DINHEIRO', 'RESERVA', 'EMPRESTIMO');
CREATE TYPE origem AS ENUM ('PIX', 'SALARIO', 'EMPRESTIMO', 'RESERVA', 'OUTRO');

CREATE TABLE CONTA (
    cpf_proprietario        BIGINT NOT NULL,
    nome_proprietario       VARCHAR(120) NOT NULL,
    dt_nasc_proprietario    DATE NOT NULL,
    telefone                BIGINT,
    email                   VARCHAR(90) NOT NULL,
    senha                   VARCHAR(256) NOT NULL,
    CONSTRAINT CONTA_PK PRIMARY KEY (cpf_proprietario),
    CONSTRAINT CONTA_email_UK UNIQUE (email),
	CONSTRAINT CONTA_cpf_proprietario_check CHECK (cpf_proprietario <= 99999999999),
	CONSTRAINT CONTA_telefone_check CHECK (telefone IS NULL OR telefone <= 99999999999)
);

CREATE TABLE RESERVA (
    id_reserva          SERIAL PRIMARY KEY,
    dt_criacao          DATE NOT NULL,
    titulo_reserva      VARCHAR(30) NOT NULL,
    descricao_reserva   VARCHAR(100),
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT RESERVA_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE SAIDA (
    id_saida            SERIAL PRIMARY KEY,
    valor_saida         DECIMAL(9,2) NOT NULL,
    categoria           categoria NOT NULL,
    descricao_saida     VARCHAR(100),
    forma_pagamento     forma_pagamento NOT NULL,
    dt_hora_saida       TIMESTAMP NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    id_reserva          BIGINT,
    CONSTRAINT SAIDA_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT SAIDA_RESERVA_FK FOREIGN KEY (id_reserva)
        REFERENCES RESERVA(id_reserva)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE LEMBRETE (
    id_lembrete         SERIAL PRIMARY KEY,
    dt_lembrete         DATE NOT NULL,
    titulo_lembrete     VARCHAR(30) NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT LEMBRETE_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE EMPRESTIMO (
    id_emprestimo       SERIAL PRIMARY KEY,
    nome_devedor        VARCHAR(120) NOT NULL,
    dt_emprestimo       DATE NOT NULL,
    dt_limite_pg        DATE,
    cpf_proprietario    BIGINT NOT NULL,
    id_saida            BIGINT NOT NULL,
    CONSTRAINT EMPRESTIMO_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT EMPRESTIMO_SAIDA_FK FOREIGN KEY (id_saida)
        REFERENCES SAIDA(id_saida)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE ENTRADA (
    id_entrada          SERIAL PRIMARY KEY,
    valor_entrada       DECIMAL(9,2) NOT NULL,
    origem              origem NOT NULL,
    descricao_entrada   VARCHAR(100),
    dt_hora_entrada     DATE NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    id_reserva          BIGINT,
    id_emprestimo       BIGINT,
    CONSTRAINT ENTRADA_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT ENTRADA_RESERVA_FK FOREIGN KEY (id_reserva)
        REFERENCES RESERVA(id_reserva)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ENTRADA_EMPRESTIMO_FK FOREIGN KEY (id_emprestimo)
        REFERENCES EMPRESTIMO(id_emprestimo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE META (
    id_meta             SERIAL PRIMARY KEY,
    valor_meta          DECIMAL(9,2) NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT META_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE GASTO_BASE (
    id_gasto_base       SERIAL PRIMARY KEY,
    titulo_gasto        VARCHAR(30) NOT NULL,
    valor_gasto         DECIMAL(9,2) NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT GASTO_BASE_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);


-- ----------------------------------------------------------------------------


CREATE DATABASE money_mastery_teste;

\c money_mastery_teste;

SET search_path TO public;

CREATE TYPE categoria AS ENUM ('LAZER', 'ALIMENTACAO', 'SAUDE', 'MORADIA',  'TRANSPORTE', 'EDUCACAO', 'OUTRO');
CREATE TYPE forma_pagamento AS ENUM ('CREDITO', 'DEBITO', 'PIX', 'DINHEIRO', 'RESERVA', 'EMPRESTIMO');
CREATE TYPE origem AS ENUM ('PIX', 'SALARIO', 'EMPRESTIMO', 'RESERVA', 'OUTRO');

CREATE TABLE CONTA (
    cpf_proprietario        BIGINT NOT NULL,
    nome_proprietario       VARCHAR(120) NOT NULL,
    dt_nasc_proprietario    DATE NOT NULL,
    telefone                BIGINT,
    email                   VARCHAR(90) NOT NULL,
    senha                   VARCHAR(256) NOT NULL,
    CONSTRAINT CONTA_PK PRIMARY KEY (cpf_proprietario),
    CONSTRAINT CONTA_email_UK UNIQUE (email),
	CONSTRAINT CONTA_cpf_proprietario_check CHECK (cpf_proprietario <= 99999999999),
	CONSTRAINT CONTA_telefone_check CHECK (telefone IS NULL OR telefone <= 99999999999)
);

CREATE TABLE RESERVA (
    id_reserva          SERIAL PRIMARY KEY,
    dt_criacao          DATE NOT NULL,
    titulo_reserva      VARCHAR(30) NOT NULL,
    descricao_reserva   VARCHAR(100),
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT RESERVA_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE SAIDA (
    id_saida            SERIAL PRIMARY KEY,
    valor_saida         DECIMAL(9,2) NOT NULL,
    categoria           categoria NOT NULL,
    descricao_saida     VARCHAR(100),
    forma_pagamento     forma_pagamento NOT NULL,
    dt_hora_saida       TIMESTAMP NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    id_reserva          BIGINT,
    CONSTRAINT SAIDA_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT SAIDA_RESERVA_FK FOREIGN KEY (id_reserva)
        REFERENCES RESERVA(id_reserva)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE LEMBRETE (
    id_lembrete         SERIAL PRIMARY KEY,
    dt_lembrete         DATE NOT NULL,
    titulo_lembrete     VARCHAR(30) NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT LEMBRETE_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE EMPRESTIMO (
    id_emprestimo       SERIAL PRIMARY KEY,
    nome_devedor        VARCHAR(120) NOT NULL,
    dt_emprestimo       DATE NOT NULL,
    dt_limite_pg        DATE,
    cpf_proprietario    BIGINT NOT NULL,
    id_saida            BIGINT NOT NULL,
    CONSTRAINT EMPRESTIMO_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT EMPRESTIMO_SAIDA_FK FOREIGN KEY (id_saida)
        REFERENCES SAIDA(id_saida)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE ENTRADA (
    id_entrada          SERIAL PRIMARY KEY,
    valor_entrada       DECIMAL(9,2) NOT NULL,
    origem              origem NOT NULL,
    descricao_entrada   VARCHAR(100),
    dt_hora_entrada     DATE NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    id_reserva          BIGINT,
    id_emprestimo       BIGINT,
    CONSTRAINT ENTRADA_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE,
    CONSTRAINT ENTRADA_RESERVA_FK FOREIGN KEY (id_reserva)
        REFERENCES RESERVA(id_reserva)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ENTRADA_EMPRESTIMO_FK FOREIGN KEY (id_emprestimo)
        REFERENCES EMPRESTIMO(id_emprestimo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE META (
    id_meta             SERIAL PRIMARY KEY,
    valor_meta          DECIMAL(9,2) NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT META_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

CREATE TABLE GASTO_BASE (
    id_gasto_base       SERIAL PRIMARY KEY,
    titulo_gasto        VARCHAR(30) NOT NULL,
    valor_gasto         DECIMAL(9,2) NOT NULL,
    cpf_proprietario    BIGINT NOT NULL,
    CONSTRAINT GASTO_BASE_CONTA_FK FOREIGN KEY (cpf_proprietario)
        REFERENCES CONTA(cpf_proprietario)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);