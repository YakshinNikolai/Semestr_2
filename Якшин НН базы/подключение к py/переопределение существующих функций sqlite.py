import sqlite3

def lower(string):
    return str(string).upper()
def get_developer_name(dev_id):
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db')
        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_connection.create_function("lower", 1, lower)
        select_query="SELECT lower(name) FROM sqlitedb_developers where id=?"
        cursor.execute(select_query, (dev_id,))
        name=cursor.fetchone()
        print("Имя разработчика", name)
        cursor.close()
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

get_developer_name(1)