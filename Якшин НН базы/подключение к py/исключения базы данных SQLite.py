import sqlite3
import traceback
import sys

try:
    sqlite_connection=sqlite3.connect('sqlite_python.db')
    cursor=sqlite_connection.cursor()
    print("База данных подключена к SQLite")

    sqlite_insert_query="""INSERT INTO unknown_table_1
           (id, text) VALUES (1, 'Демо текст')"""


    count=cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Запись успешно вставлена в таблицу sqlitedb_developers", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Не удалось вставить данные в таблицу sqlite")
    print("Класс исключения:", error.__class__)
    print("Исключение", error.args)
    print("Печать подробностей исключения SQLite: ")
    exc_type, exc_value, exc_tb=sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

