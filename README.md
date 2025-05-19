# Prueba Técnica R1 - ETL con Python y MySQL

Este repositorio contiene el desarrollo de una ETL usando Python y una base de datos MySQL local, cumpliendo con los siguientes requerimientos técnicos:

## Requisitos 

1. **Base de datos local**: `python_test` creada en MySQL (XAMPP).
2. **Tablas relacionadas**: `autor` y `libro`, relacionadas por la columna `id_autor`.
3. **Extracción** de datos desde archivos Excel.
4. **Transformación** de datos (limpieza y formateo).
5. **Carga** de datos a la base de datos tras eliminar registros existentes.
6. **Repositorio público en GitHub** con archivos fuente y pasos documentados.

---

---

## Estructura del proyecto

```
prueba_tecnica_R1/
│
├── data/
│   ├── autores.xlsx
│   └── libros.xlsx
│
├── crear_bd_mysql.sql
├── etl_carga_autores_libros.py
└── README.md
```


---

## Requisitos previos

### Software necesario

- Python 3.x instalado
- XAMPP o MySQL local en funcionamiento
- Git (opcional, si deseas clonar el repositorio directamente)

### Librerías de Python

Instálalas con pip:

```bash
pip install pandas pymysql openpyxl
```

## Paso a paso para ejecutar el Job ETL

## 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/tu_usuario/prueba_tecnica_R1.git
cd prueba_tecnica_R1
```

## 2. Crear la base de datos y las tablas

Opción 1: Ejecutar el script SQL incluido

Entra a phpMyAdmin (XAMPP) o tu cliente de MySQL y ejecuta el contenido del archivo:

```bash
create_database.sql
```

Opción 2: Manualmente en phpMyAdmin

```bash
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
```

## 3. Verifica los archivos de datos
Asegúrate de que los archivos autores.xlsx y libros.xlsx están en la carpeta data/. Puedes revisar o modificar los datos allí.

## 4. Ejecutar el script ETL

Desde la raíz del proyecto, ejecuta:


```bash
python etl_carga_autores_libros.py
```

## ¿Qué hace el script?

- Conecta a la base de datos python_test.
- Lee los datos desde los archivos Excel.
- Aplica transformaciones: limpieza de nombres, capitalización de títulos.
- Elimina todos los registros existentes en las tablas.
- Inserta los nuevos datos desde los Excel.

## Resultado esperado

Al ejecutar el script, deberías ver algo como:

```bash
Conectando...
Conexión creada
ETL completado exitosamente.
```

Los datos insertados serán visibles si consultas las tablas en MySQL.