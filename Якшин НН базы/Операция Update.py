import psycopg2
from psycopg2 import Error

def update_table(mobile_id, price):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # Пароль, который указали при установке PostgreSQL
                                      password="031995",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
    
        cursor=connection.cursor()
        print("Таблица до обновления записи")
        sql_select_query="""select * from mobile where id=%s"""
        cursor.execute(sql_select_query, (mobile_id,))
        record=cursor.fetchone()
        print(record)

        # Обновление отдельной записи
        sql_update_query="""Update mobile set price =%s where id=%s"""
        cursor.execute(sql_update_query, (price, mobile_id,))
        connection.commit()
        count=cursor.rowcount
        print(count, "Запись успешно добавлена")

        print("Таблица после обновления записи")
        sql_select_query="""select * from mobile where id=%s"""
        cursor.execute(sql_select_query, (mobile_id,))
        record=cursor.fetchone()
        print(record)

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

update_table(5, 970)
    