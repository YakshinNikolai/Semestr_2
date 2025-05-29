import  sqlite3

def update_multiple_records(record_list):
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db')
        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_update_query="""Update sqlitedb_developers set salary=? where id=?"""
        cursor.executemany(sqlite_update_query, record_list)
        sqlite_connection.commit()
        print("Записей", cursor.rowcount, ".Успешно обновлены")
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

records_to_update=[(9700, 4), (7800, 5), (8400, 6)]
update_multiple_records(records_to_update)