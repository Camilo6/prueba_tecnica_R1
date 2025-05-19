# 🧪 Prueba Técnica R1 - ETL con Python y MySQL

Este repositorio contiene el desarrollo de una ETL usando Python y una base de datos MySQL local, cumpliendo con los siguientes requerimientos técnicos:

## 📋 Requisitos cumplidos

1. **Base de datos local**: `python_test` creada en MySQL (XAMPP).
2. **Tablas relacionadas**: `autor` y `libro`, relacionadas por la columna `id_autor`.
3. **Extracción** de datos desde archivos Excel.
4. **Transformación** de datos (limpieza y formateo).
5. **Carga** de datos a la base de datos tras eliminar registros existentes.
6. **Repositorio público en GitHub** con archivos fuente y pasos documentados.

---

## ⚙️ Requisitos previos

Antes de ejecutar el script, asegúrate de tener instalado:

- Python 3.x
- MySQL (se recomienda usar XAMPP)
- Librerías de Python:
  ```bash
  pip install pandas pymysql openpyxl
