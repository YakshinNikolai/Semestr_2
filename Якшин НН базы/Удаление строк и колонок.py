import psycopg2
from psycopg2 import Error

def delete_data(mobile_id):
    try:
         # Подключиться к существующей базе данных
         connection = psycopg2.connect(user="postgres",
                                       # Пароль, который указали при установке PostgreSQL
                                       password="031995",
                                       host="127.0.0.1",
                                       port="5432",
                                       database="postgres_db")
    
         cursor=connection.cursor()
         # Удаление записи
         sql_delete_query="Delete from mobile where id=%s"
         cursor.execute(sql_delete_query, (mobile_id,))
         connection.commit()
         count=cursor.rowcount
         print(count, "Запись успешно удалена")

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

delete_data(5)
delete_data(6)

    