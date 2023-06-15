import sqlite3

conn=sqlite3.connect('C:/Users/PC/Desktop/Python/Python/Tema11/Ejercicio1/mydbtema11.db')
cursor=conn.cursor()

rows=cursor.execute('SELECT*FROM Alumnos WHERE Nombre="Lara"')
for row in rows:
    print(row)

cursor.close()
conn.close()