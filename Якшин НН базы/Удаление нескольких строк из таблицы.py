import psycopg2
from psycopg2 import Error

def delete_in_bulk(records):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # Пароль, который указали при установке PostgreSQL
                                      password="031995",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
    
        cursor=connection.cursor()
        # Удалить несколько записей
        delete_query="""Delete from mobile where id=%s"""
        cursor.executemany(delete_query, records)
        connection.commit()

        row_count=cursor.rowcount
        print(row_count, "Записи удалены")

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

            
delete_in_bulk([(1,), (2,), (14,)])