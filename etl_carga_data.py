import pymysql
import pandas as pd

print("Conectando...")
try:
    # Conexión base de datos
    conn = pymysql.connect(
        host="localhost",
        port=3306,  # cambia si es necesario
        user="root",
        password="",
        database="python_test",
        connect_timeout=5
    )
    print("Conexión creada")

    cursor = conn.cursor()

    # Cargar Excel 
    autores_df = pd.read_excel("data/autores.xlsx")
    libros_df = pd.read_excel("data/libros.xlsx")

    # Transformación de los datos
    autores_df['nombre'] = autores_df['nombre'].str.strip()
    libros_df['titulo'] = libros_df['titulo'].str.title()

    # Eliminar datos existentes
    cursor.execute("DELETE FROM libro")
    cursor.execute("DELETE FROM autor")
    conn.commit()

    # Insertar nuevos datos 
    for _, row in autores_df.iterrows():
        cursor.execute(
            "INSERT INTO autor (id_autor, nombre, pais) VALUES (%s, %s, %s)",
            (int(row['id_autor']), row['nombre'], row['pais'])
        )

    for _, row in libros_df.iterrows():
        cursor.execute(
            "INSERT INTO libro (id_libro, titulo, anio, id_autor) VALUES (%s, %s, %s, %s)",
            (int(row['id_libro']), row['titulo'], int(row['anio']), int(row['id_autor']))
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("ETL completado exitosamente.")

except Exception as e:
    print(f"Error: {e}")
