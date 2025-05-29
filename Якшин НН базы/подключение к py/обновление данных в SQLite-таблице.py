import sqlite3

def update_sqlite_table():
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db ')
        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query="""Update sqlitedb_developers set salary=10000 where id=4"""
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибки при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

update_sqlite_table()