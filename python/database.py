
import sqlite3

sqliteConnection = sqlite3.connect('database.db')
cursor = sqliteConnection.cursor()



def insertFaceid(faceid,date,age):
    cursor.execute('insert into users(faceid,date,age) values(?,?,?)',(str(faceid),date,age))
    sqliteConnection.commit()

def readUsers():
    query = 'select * from users'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def saveEmotion(detectName,emotion,date):
    try:
        query = f"select * from users where faceid={detectName}"
        cursor.execute(query)
        result = cursor.fetchall()
        if(len(result)>0):
            userid=result[0][0]
            cursor.execute('insert into emotions(user_id,emotion,date) values(?,?,?)',(userid,str(emotion),date))
            sqliteConnection.commit()
            return True
    except:
        return False

    return False

saveEmotion("437252","sad","")