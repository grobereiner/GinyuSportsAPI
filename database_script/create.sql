-- CREATE DATABASE ginyu;
CREATE SCHEMA IF NOT EXISTS ginyu;
SET search_path = ginyu;

CREATE TABLE resultados (
    id SERIAL,
    fecha DATE,
    team_one VARCHAR(50),
    team_two VARCHAR(50),
    resultado VARCHAR(5),
    pais VARCHAR(50)
);

ALTER TABLE resultados ADD CONSTRAINT resultados_pk PRIMARY KEY(id);

-- TEST INSERTION
INSERT INTO resultados (fecha, team_one, team_two, resultado)
VALUES (
    '5/27/2022', 'Cienciano', 'Alianza', '4-4');

