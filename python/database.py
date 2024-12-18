
import sqlite3

sqliteConnection = sqlite3.connect('database.db')
cursor = sqliteConnection.cursor()



def insert(faceid,date,age):
    cursor.execute('insert into users(faceid,date,age) values(?,?,?)',(str(faceid),date,age))
    sqliteConnection.commit()

def select():
    query = 'select * from users'
    cursor.execute(query)
    result = cursor.fetchall()
    return result
