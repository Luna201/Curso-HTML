import mysql.connector
from mysql.connector import cursor

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

mi_cursor = personas_db()
mi_cursor.execute("SELECT * FROM personas")
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)