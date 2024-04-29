import csv
import psycopg2 as pgsql


with pgsql.connect(host="localhost", dbname="postgres", user="postgres", password="mumbik112233", port=5433, options="-c client_encoding=utf-8") as connection:
    with connection.cursor() as cur:
        
        cur.execute("""CREATE TABLE IF NOT EXISTS Contacts (
            last_name VARCHAR(255),
            first_name VARCHAR(255),
            phone_number VARCHAR(20)  -- Изменяем тип данных на VARCHAR
        );
        """)


        def update_contact(last_name, attribute, new_value):
            try:
                cur.execute("""UPDATE Contacts
                SET {} = %s
                WHERE last_name = %s
                """.format(attribute), (new_value, last_name))
                connection.commit()
            except pgsql.Error as e:
                print(f"Ошибка при обновлении контакта: {e}")

        def delete_contact(last_name):
            try:
                cur.execute("""DELETE FROM Contacts
                WHERE last_name=%s
                """, (last_name,))
                connection.commit()
            except pgsql.Error as e:
                print(f"Ошибка при удалении контакта: {e}")

        def enter_data():
            last_name = input("Enter last name: ")
            first_name = input("Enter first name: ")
            phone_number = input("Enter phone number: ")
            try:
                cur.execute("""INSERT INTO Contacts (last_name, first_name, phone_number) VALUES (%s, %s, %s)""", (last_name, first_name, phone_number))
                connection.commit()
            except pgsql.Error as e:
                print(f"Ошибка при добавлении контакта: {e}")

        def insert_from_csv(file_name):
            try:
                with open(file_name + '.csv', 'r') as f:
                    reader = csv.reader(f)
                    next(reader)  
                    cur.executemany("INSERT INTO Contacts (last_name, first_name, phone_number) VALUES (%s, %s, %s)", reader)
                connection.commit()
            except pgsql.Error as e:
                print(f"Ошибка при вставке данных из CSV: {e}")

        
        while True:
            print("Type 'add' to enter data manually or 'stop' to break")
            mode = input()
            if mode == "stop":
                break
            elif mode == "add":
                enter_data()

      
        while True:
            print("Want to insert data from csv file? yes/no:")
            mode = input()
            if mode == "no":
                break
            print("Enter the name of the file")
            file_name = input()
            insert_from_csv(file_name)

        while True:
            print("Type 'update' to update some data or 'stop' to break")
            mode = input()
            if mode == "stop":
                break
            try:
                cur.execute("""SELECT * FROM Contacts""")
                print(cur.fetchall())
                print("Enter last name")
                last_name = input()
                print("What you want to change? first_name/phone_number")
                attribute = input()
                print("Enter new first name/phone number")
                new_value = input()
                update_contact(last_name, attribute, new_value)
            except pgsql.Error as e:
                print(f"Ошибка при обновлении данных: {e}")

        while True:
            print("Want to delete some data? yes/no")
            mode = input()
            if mode == "no":
                break
            try:
                cur.execute("""SELECT * FROM Contacts""")
                print(cur.fetchall())
                print("Enter last name")
                last_name = input()
                delete_contact(last_name)
            except pgsql.Error as e:
                print(f"Ошибка при удалении данных: {e}")
