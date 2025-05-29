import psycopg2
from psycopg2 import Error

try:
    #Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
        # Пароль, который указали при установке PostgreSQL
        password="031995",
        host="127.0.0.1",
        port="5432",
        database="postgres_db")
    # Создайте курсор для выполнения операций с базой данных 
    cursor=connection.cursor()
    # SQL-запрос для создания новой таблицы
    create_table_query='''CREATE TABLE item (
           item_id serial NOT  NULL PRIMARY KEY,
           item_name VARCHAR(100) NOT NULL, 
           purchase_time timestamp NOT NULL,
           price INTEGER NOT NULL
           );'''
    # Выполнение команды: это создаёт новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")

