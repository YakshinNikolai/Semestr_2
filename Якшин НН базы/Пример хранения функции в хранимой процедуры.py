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
    cursor=connection.cursor()
    # хранимая процедура
    cursor.callproc('filter_by_price', [999,])

    print("Записи с ценой меньше или равной 999")
    result=cursor.fetchall()
    for row in result:
        print("Id =", row[0],)
        print("Model =", row[1])
        print("Price =", row[2])

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")