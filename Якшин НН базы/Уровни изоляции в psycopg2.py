import psycopg2
from psycopg2 import pool

try:
    # Подключиться к существующей базе данных
    postgresql_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
        user="postgres",
        # пароль, который указали при установке PostgreSQL
        password="031995",
        host="127.0.0.1",
        port="5432",
        database="postgres_db")

    if postgresql_pool:
        print("Пул соединений создан успешно")

    # Используйте getconn() для получения соединения из пула соединений
    connection = postgresql_pool.getconn()

    if connection:
        print("Соединение установлено")
        cursor = connection.cursor()
        cursor.execute("select * from mobile")
        mobile_records = cursor.fetchall()

        print("Отображение строк с таблицы mobile")
        for row in mobile_records:
            print(row)

        cursor.close()

        # Используйте этот метод, чтобы отпустить объект соединения
        # и отправить обратно в пул соединений
        postgresql_pool.putconn(connection)
        print("PostgreSQL соединение вернулось в пул")

except (Exception, psycopg2.DatabaseError) as error:
    print("Ошибка при подключении к PostgreSQL", error)
finally:
    if postgresql_pool:
        postgresql_pool.closeall()
    print("Пул соединений PostgreSQL закрыт")