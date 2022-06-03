-- CREATE DATABASE ginyu;

CREATE TABLE resultados (
    id SERIAL,
    fecha DATE,
    team_one VARCHAR(50),
    team_two VARCHAR(50),
    resultado VARCHAR(5)
);

ALTER TABLE resultados ADD CONSTRAINT resultados_pk PRIMARY KEY(id);

