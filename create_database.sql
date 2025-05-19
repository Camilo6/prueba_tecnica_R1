CREATE DATABASE python_test;

USE python_test;

CREATE TABLE Autor (
    id_autor INT PRIMARY KEY,
    nombre VARCHAR(100),
    pais VARCHAR(100)
);

CREATE TABLE Libro (
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(200),
    anio INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
);
