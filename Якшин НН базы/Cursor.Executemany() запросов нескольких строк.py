import psycopg2
from psycopg2 import Error

def bulk_insert(records):
    try:
         # Подключиться к существующей базе данных
         connection = psycopg2.connect(user="postgres",
                                       # Пароль, который указали при установке PostgreSQL
                                       password="031995",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="postgres_db")
    
         cursor=connection.cursor()
         sql_insert_query="""INSERT INTO mobile (id, model, price)
                        VALUES (%s, %s, %s)"""
         
         # executemany() для вставки нескольких строк
         result=cursor.executemany(sql_insert_query, records)
         connection.commit()
         print(cursor.rowcount, "Запись(и) успешно вставлена(ы) в таблицу mobile")

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

records_to_insert=[ (13, 'LG', 800), (14, 'One Plus 6', 950)]
bulk_insert(records_to_insert)
    