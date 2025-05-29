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
    postgres_insert_query="""INSERT INTO mobile (ID, MODEL, PRICE)
                       VALUES (%s,%s,%s)"""
    record_to_insert=(9,'One Plus 6', 950)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count=cursor.rowcount
    print(count, "Запись успешно добавлена в таблицу mobile")

except(Exception, Error) as error:
   print("Ошибка при работе с PostgreSQL", error)
finally:
   if connection:
      cursor.close()
      connection.close()
      print("Соединение с PostgreSQL закрыто")
