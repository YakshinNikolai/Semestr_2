import sqlite3

def get_developer_info(id):
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db')
        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_select_query="""select * from sqlitedb_developers where id=?"""
        cursor.execute(sql_select_query,(id,))
        records=cursor.fetchall()
        print("Вывод ID", id)
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

get_developer_info(2)           

            

