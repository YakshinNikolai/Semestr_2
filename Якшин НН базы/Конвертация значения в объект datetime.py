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
    insert_query="""INSERT INTO item (item_id, item_name, purchase_time, price)
                VALUES (%s, %s, %s, %s)"""
    item_purchase_time=datetime.datetime.now()
    item_tuple=(13, "Keyboard", item_purchase_time, 150) 
    cursor.execute(insert_query, item_tuple)
    connection.commit()
    print("1 элемент успешно добавлен")

    # Считать значение времени покупки PostgreSQL в Python datetime
    cursor.execute("SELECT purchase_time from item where item_id=13")
    purchase_datetime=cursor.fetchone()
    print("Дата покупки товара", purchase_datetime[0].date())
    print("Время покупки товара", purchase_datetime[0].time())

except(Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")


