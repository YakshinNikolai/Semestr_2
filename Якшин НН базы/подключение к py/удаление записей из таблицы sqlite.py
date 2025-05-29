import sqlite3

def delete_record():
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db')
        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_delete_query="""DELETE from sqlitedb_developers where id=6"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

delete_record()