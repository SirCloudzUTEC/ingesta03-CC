CREATE DATABASE IF NOT EXISTS bd_ingesta;
USE bd_ingesta;

CREATE TABLE IF NOT EXISTS personas (
  id INT PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  edad INT
);

INSERT INTO personas VALUES
  (1, 'geraldo', 'colchado', 20),
  (2, 'juan', 'salas', 15),
  (3, 'pedro', 'gamarra', 35);
