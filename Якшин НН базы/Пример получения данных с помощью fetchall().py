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
    postgreSQL_select_Query="select * from mobile"

    cursor.execute(postgreSQL_select_Query)
    print("Выбор сторок из таблицы mobile с помощью cursor.fetchall")
    mobile_records=cursor.fetchall()

    print("Вывод каждой строки и её столбцов")
    for row in mobile_records:
        print("Id =", row[0],)
        print("Модель =", row[1],)
        print("Ценв =", row[2], "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")