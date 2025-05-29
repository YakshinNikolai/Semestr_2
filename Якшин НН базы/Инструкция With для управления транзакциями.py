import psycopg2
from psycopg2 import Error
connection = psycopg2.connect(**params)
with connection:
    with connection.cursor() as cursor:
        # Поиск цены товара
        query = """select price from itemstable where itemid = 876"""
        cursor.execute(query)
        record = cursor.fetchone()[0]
        item_price = int(record)

        # Получение остатка на счету
        query = """select balance from evallet where userId = 23"""
        cursor.execute(query)
        record = cursor.fetchone()[0]
        evallet_balance = int(record)
        new_evallet_balance -= item_price

        # Обновление баланса с учетом расхода
        sql_update_query = """Update evallet set balance = %s where id = 23"""
        cursor.execute(sql_update_query(new_evallet_balance,))

        # Зачисление на баланс компании
        query = """select balance from account where accountId = 2236781258763"""
        cursor.execute(query)
        record = cursor.fetchone()
        account_balance = int(record)
        new_account_balance += item_price

        # Обновление счета компании
        sql_update_query = """Update account set balance = %s where id = 132456"""
        cursor.execute(sql_update_query, (new_account_balance,))
        print("Транзакция успешно завершена")