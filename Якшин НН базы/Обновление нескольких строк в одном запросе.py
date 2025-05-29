import psycopg2
from psycopg2 import Error

def update_in_bulk(records):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # Пароль, который указали при установке PostgreSQL
                                      password="031995",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
    
        cursor=connection.cursor()
        # Обновить несколько записей
        sql_update_query="""Update mobile set price=%s where id=%s"""
        cursor.executemany(sql_update_query, records)
        connection.commit()

        row_count=cursor.rowcount
        print(row_count, "Записи обновлены")

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

            
update_in_bulk([(750, 13), (950, 14)])
    