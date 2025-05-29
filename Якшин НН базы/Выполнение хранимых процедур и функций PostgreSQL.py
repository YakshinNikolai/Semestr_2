import psycopg2
from psycopg2 import Error

def create_func(query):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # Пароль, который указали при установке PostgreSQL
                                      password="031995",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
    
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")    

postgresql_func = """
CREATE OR REPLACE FUNCTION filter_by_price(max_price integer)
RETURNS TABLE(id INT, model TEXT, price REAL) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM mobile where mobile.price <= max_price;
END;
$$ LANGUAGE plpgsql;
"""

create_func(postgresql_func)