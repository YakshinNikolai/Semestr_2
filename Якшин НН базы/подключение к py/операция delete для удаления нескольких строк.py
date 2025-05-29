import sqlite3

def delete_multiple_records(ids_list):
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db')
        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_update_query="""DELETE from sqlitedb_developers where id=?"""
        cursor.executemany(sqlite_update_query, ids_list)
        sqlite_connection.commit()
        print("Удалено записей:", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

ids_to_delete=[(4,),(3,)]
delete_multiple_records(ids_to_delete)
