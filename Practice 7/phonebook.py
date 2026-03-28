import csv
from connect import connect

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        phone_number VARCHAR(20) UNIQUE NOT NULL
    );
    """
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()

def import_from_csv(filename):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cur.execute(
                        "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                        (row['first_name'], row['phone_number'])
                    )
            conn.commit()

def add_contact(name, phone):
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
                conn.commit()
    except Exception as e:
        print(f"Error: {e}")

def update_contact(old_name, new_name=None, new_phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
            if new_phone:
                cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (new_phone, old_name))
            conn.commit()

def query_contacts(filter_val):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone_number LIKE %s", 
                        (f"%{filter_val}%", f"{filter_val}%"))
            for row in cur.fetchall():
                print(row)

def delete_contact(identifier):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone_number = %s", (identifier, identifier))
            conn.commit()

def main():
    create_table()
    while True:
        print("\n1. Import CSV\n2. Add\n3. Update\n4. Search\n5. Delete\n6. Exit")
        choice = input("Choice: ")
        if choice == '1':
            import_from_csv('contacts.csv')
        elif choice == '2':
            add_contact(input("Name: "), input("Phone: "))
        elif choice == '3':
            update_contact(input("Name to update: "), input("New name: "), input("New phone: "))
        elif choice == '4':
            query_contacts(input("Search term: "))
        elif choice == '5':
            delete_contact(input("Name or Phone: "))
        elif choice == '6':
            break

if __name__ == "__main__":
    main()