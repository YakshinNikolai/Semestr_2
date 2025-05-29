import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    #Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
        # ПарольБ который указали при установке PostgreSQL
        password="031995",
        host="127.0.0.1",
        port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE postgres_db")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")