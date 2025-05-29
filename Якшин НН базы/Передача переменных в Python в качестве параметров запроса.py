import psycopg2
from psycopg2 import Error

def get_mobile_details(mobile_id):
    try:
         # Подключиться к существующей базе данных
         connection = psycopg2.connect(user="postgres",
                                       # Пароль, который указали при установке PostgreSQL
                                       password="031995",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="postgres_db")
    
         cursor=connection.cursor()
         postgresql_select_query="select * from mobile where id=%s"

         cursor.execute(postgresql_select_query, (mobile_id,))
         mobile_records=cursor.fetchall()

         for row in mobile_records:
             print("Id =", row[0],)
             print("Модель =", row[1])
             print("Цена =", row[2])

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

get_mobile_details(1)
get_mobile_details(5)
