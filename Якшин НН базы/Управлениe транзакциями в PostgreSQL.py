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
    
    connection.autocommit=False
    cursor=connection.cursor()
    amount=200

    query="""select price from mobile where id=15"""
    cursor.execute(query)
    record=cursor.fetchone() [0]
    price_a =int(record)
    price_a -=amount

    # Понизить цену у первого
    sql_update_query="""update mobile set price = %s where id=15"""
    cursor.execute(sql_update_query, (price_a,))

    query="""select price from mobile where id = 16"""
    cursor.execute(query)
    record=cursor.fetchone() [0]
    price_b=int(record)
    price_b += amount

     # Повысить цену у первого
    sql_update_query="""Update mobile set price = %s where id=16"""
    cursor.execute(sql_update_query, (price_b,))

    # совершение транзакции
    connection.commit()
    print("Транзакция успешно завершена")

except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")