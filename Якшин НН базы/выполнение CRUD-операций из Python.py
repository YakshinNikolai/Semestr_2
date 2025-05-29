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
    # Выполнение SQL-запроса для вставки данных в таблицу
    insert_query="""INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 запись успешно вставлена")
    # Получить результат
    cursor.execute("SELECT * from mobile")
    record=cursor.fetchall()
    print("Результат", record)

    # Выполнение SQL-запроса для обновления таблицы
    update_query="""Update mobile set price = 1500 where id=1"""
    cursor.execute(update_query)
    connection.commit()
    count=cursor.rowcount
    print(count, "Запись успешно удалена")
    # Получить результат
    cursor.execute("SELECT * from mobile")
    print("Результат", cursor.fetchall())

except(Exception, Error) as error:
   print("Ошибка при работе с PostgreSQL", error)
finally:
   if connection:
      cursor.close()
      connection.close()
      print("Соединение с PostgreSQL закрыто")
