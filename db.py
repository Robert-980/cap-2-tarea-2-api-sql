import sqlite3
from datetime import datetime

# Conexión a la base de datos (se creará si no existe)
conn = sqlite3.connect('database.db')

# Crear un cursor para ejecutar comandos SQL
cur = conn.cursor()

# Crear la tabla 'database'
cur.execute('''
CREATE TABLE IF NOT EXISTS database (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')

# Lista de alumnos a insertar
database = [
    ('titulo1', 'contenido1'),
    ('titulo2', 'contenido2'),
    ('titulo3', 'contenido3'),
    ('titulo4', 'contenido4'),
    ('titulo5', 'contenido5')
]

# Insertar los registros en la tabla 'database'
cur.executemany('''
    INSERT INTO database (title, content)
    VALUES (?, ?)
''', database)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada y registros insertados correctamente.")