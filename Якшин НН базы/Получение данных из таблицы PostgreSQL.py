import psycopg2
import datetime
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
        # Пароль, который указали при установке PostgreSQL
        password="031995",
        host="127.0.0.1",
        port="5432",
        database="postgres_db")
    
    cursor=connection.cursor()
    # Выполнение SQL-запроса для вставки даты и времени в таблицу
    insert_query="""INSERT INTO mobile (ID, MODEL, PRICE) VALUES
                    (5, 'Iphone 12', 1000),
                    (6, 'Google Pixel 2', 700),
                    (7, 'Samsung Galaxy S21', 900),
                    (8, 'Nokia', 800),
                    (15, 'Nokia A55', 700),
                    (16, 'Tecno Camon 40', 900)"""
    cursor.execute(insert_query)
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")
