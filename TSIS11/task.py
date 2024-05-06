import psycopg2
import csv
from tabulate import tabulate 

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="mumbik112233", port=5433)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Phonebook2 (
      user_id SERIAL PRIMARY KEY,
      last_name VARCHAR(255) NOT NULL,
      first_name VARCHAR(255) NOT NULL, 
      phone_number VARCHAR(255) NOT NULL
)
""")

def insert_data():
    print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
    method = input().lower()
    if method == "con":
        last_name = input("last_name: ")
        first_name = input("first_name: ")
        phone_number = input("phone_number: ")
        cur.execute("INSERT INTO Phonebook2 (last_name, first_name, phone_number) VALUES (%s, %s, %s)", (last_name, first_name, phone_number))
    elif method == "csv":
        filepath = input("Enter a file path with proper extension: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                cur.execute("INSERT INTO Phonebook2 (last_name, first_name, phone_number) VALUES (%s, %s, %s)", tuple(row))

def update_data():
    column = input('Type the name of the column that you want to change: ')
    value = input(f"Enter {column} that you want to change: ")
    new_value = input(f"Enter the new {column}: ")
    cur.execute(f"UPDATE Phonebook2 SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

def delete_data():
    phone_number = input('Type phone number which you want to delete: ')
    cur.execute("DELETE FROM Phonebook2 WHERE phone_number = %s", (phone_number,))
    conn.commit()
    
def query_data():
    column = input("Type the name of the column which will be used for searching data: ")
    value = input(f"Type {column} of the user: ")
    cur.execute(f"SELECT * FROM Phonebook2 WHERE {column} = %s", (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "last_name", "first_name", "phone_number"]))

def display_data():
    cur.execute("SELECT * from Phonebook2;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "last_name", "first_name", "phone_number"], tablefmt='fancy_grid'))

while True:
    print("""
    List of the commands:
    1. Type "i" to INSERT
    2. Type "u" to UPDATE
    3. Type "q" to make specific QUERY 
    4. Type "d" to DELETE 
    5. Type "s" to see the values 
    6. Type "f" to close the program.
    """)

    command = input().lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "f":
        break

conn.commit()
cur.close()
conn.close()