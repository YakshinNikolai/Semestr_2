import sqlite3, datetime

def add_developer(dev_id, name, goining_data,):
    try:
        sqlite_connection=sqlite3.connect('sqlite_python.db',
                          detect_types=sqlite3.PARSE_DECLTYPES |
                          sqlite3.PARSE_COLNAMES)

        cursor=sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_create_table_query="""CREATE  TABLE new_developers2 (
                             id INTEGER PRIMARY KEY,
                             name TEXT NOT NULL,
                             goiningData timestamp);"""
        
        cursor=sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)

        # вставить данные разработчика
        sqlite_insert_with_param="""INSERT INTO 'new_developers2'
                   ('id', 'name', 'goiningData')
                   VALUES (?,?,?);"""
        
        data_tuple=(dev_id, name, goining_data)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Разработчик успешно добавлен \n")

        # получить данные разработчика
        sqlite_select_query="""SELECT name, goiningData from new_developers2 where id=?"""
        cursor.execute(sqlite_select_query, (1,))
        records=cursor.fetchall()

        for row in records:
            developer=row[0]
            goining_data=row[1]
            print(developer, "присоединился", (goining_data))
            print("тип данных", type(goining_data))
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

add_developer(1, 'Mark', datetime.datetime.now())









        