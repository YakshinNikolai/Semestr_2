import psycopg2
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
    postgresql_select_query="select * from mobile"

    cursor.execute(postgresql_select_query)

    mobile_records_one=cursor.fetchone()
    print("Вывод  первой записи", mobile_records_one)

    
    mobile_records_two=cursor.fetchone()
    print("Вывод  первой записи", mobile_records_two)

except(Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")


