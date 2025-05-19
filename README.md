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

prueba_tecnica_R1/
│
├── data/
│ ├── autores.xlsx
│ └── libros.xlsx
│
├── crear_bd_mysql.sql # Script para crear la BD y las tablas
├── etl_carga_autores_libros.py
└── README.md


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

