import sqlite3

try:
    sqlite_connection=sqlite3.connect('sqlite_python.db')
    cursor=sqlite_connection.cursor()
    print("Подключен к SQLite")

    sqlite_insert_query="""INSERT INTO sqlitedb_developers
         (id, name, email, goining_data, salary)
         VALUES (4, 'Sofia', 'sofa23469@gmail.com', '2020-11-20', 8600);"""
    cursor.execute(sqlite_insert_query)

    sql_update_query="""Update sqlitedb_developers set salary = 10000 where id=4"""
    cursor.execute(sql_update_query)

    sql_delete_query="""DELETE from sqlitedb_developers where id=4"""
    cursor.execute(sql_delete_query)

    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if(sqlite_connection):
        print("Всего строк, изменёных после подключения к базе данных: ", 
    sqlite_connection.total_changes)
        sqlite_connection.close()
        print("Соединение в SQLite закрыто")