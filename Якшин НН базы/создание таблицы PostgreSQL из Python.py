import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    #Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
        # ПарольБ который указали при установке PostgreSQL
        password="031995",
        host="127.0.0.1",
        port="5432",
        database="postgres_db")
    
    # Создайте курсор для выполения операций с базой данных
    cursor=connection.cursor()
    # SQL-запрос для создания новой таблицы
    create_table_query='''CREATE TABLE mobile
              (ID INT PRIMARY KEY   NOT NULL,
              MODEL   TEXT   NOT NULL,
              PRICE    REAL);'''
    # Выполнение команды: это создаёт новую  таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")
except(Exception, Error) as error:
   print("Ошибка при работе с PostgreSQL", error)
finally:
   if connection:
      cursor.close()
      connection.close()
      print("Соединение с PostgreSQL закрыто")


