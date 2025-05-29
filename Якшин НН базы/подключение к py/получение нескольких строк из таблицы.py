import sqlite3

def read_limited_rows(row_size):
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db')
        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query="""SELECT * from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        print("Чтение", row_size, "строк")
        records=cursor.fetchmany(row_size)
        print("Вывод каждой строки \n")
        for row in records:
            print("ID:", row[0])
            print("Имя:", row[1])
            print("Почта:", row[2])
            print("Добавлен:", row[3])
            print("Зарплата:", row[4], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

read_limited_rows(2)