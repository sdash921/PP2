import os
import psycopg2
from connect import get_connection

def run_sql_file(filename):
    """Функция для выполнения SQL скриптов с правильным путем к файлу"""
    # Получаем путь к папке, в которой лежит сам скрипт phonebook.py
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Соединяем путь к папке с именем файла
    file_path = os.path.join(base_path, filename)
    
    with open(file_path, 'r') as f:
        sql = f.read()
        
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()

def main():
    # 1. Создаем таблицу (если ее нет)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    phone VARCHAR(20)
                );
            """)
        conn.commit()

    # 2. Загружаем функции и процедуры в БД
    print("--- Загрузка функций и процедур ---")
    run_sql_file('functions.sql')
    run_sql_file('procedures.sql')

    with get_connection() as conn:
        with conn.cursor() as cur:
            
            # --- СЦЕНАРИЙ 1: Массовая вставка (Bulk Insert) ---
            print("\n--- Тест 1: Массовая вставка ---")
            names = ["Alice", "Bob", "Charlie", "Dave"]
            phones = ["123456", "654321", "111", "999999"] # "111" слишком короткий, должен отсеяться
            cur.execute("CALL bulk_insert_contacts(%s, %s)", (names, phones))
            print("Массовая вставка выполнена (см. NOTICE в консоли базы, если есть).")

            # --- СЦЕНАРИЙ 2: Upsert (Обновление или Вставка) ---
            print("\n--- Тест 2: Upsert (обновление Alice) ---")
            cur.execute("CALL upsert_contact(%s, %s)", ("Alice", "000000"))
            print("Alice обновлена новым номером.")

            # --- СЦЕНАРИЙ 3: Поиск по шаблону ---
            print("\n--- Тест 3: Поиск 'Ali' ---")
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", ("Ali",))
            print("Результат:", cur.fetchall())

            # --- СЦЕНАРИЙ 4: Пагинация ---
            print("\n--- Тест 4: Пагинация (первые 2 записи) ---")
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (2, 0))
            print("Результат:", cur.fetchall())

            # --- СЦЕНАРИЙ 5: Удаление ---
            print("\n--- Тест 5: Удаление Dave ---")
            cur.execute("CALL delete_contact(%s)", ("Dave",))
            print("Dave удален.")

            conn.commit()
            print("\nВсе тесты успешно пройдены!")

if __name__ == "__main__":
    main()