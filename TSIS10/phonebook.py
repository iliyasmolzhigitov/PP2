import csv
import psycopg2 as pgsql

connection = pgsql.connect(host="localhost", dbname="postgres", user="postgres", 
                           password="baha2710", port=5432)
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Contacts (
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    phone_number INT
);
""")

def update_contact(last_name, attribute, new_value):
    cur.execute("""UPDATE Contacts
    SET {} = '{}'
    WHERE last_name = '{}'
    """.format(attribute, new_value, last_name))

def delete_contact(last_name):
    cur.execute("""DELETE FROM Contacts
    WHERE last_name='{}'
    """.format(last_name))

def enter_data():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    phone_number = input("Enter phone number: ")
    cur.execute("""INSERT INTO Contacts (last_name, first_name, phone_number) VALUES (%s, %s, %s)""", (last_name, first_name, phone_number))

def insert_from_csv(file_name):
    with open(file_name + '.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO Contacts VALUES (%s, %s, %s)", row)

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
    cur.execute("""SELECT * FROM Contacts""")
    print(cur.fetchall())
    print("Enter last name")
    last_name = input()
    print("What you want to change? first_name/phone_number")
    attribute = input()
    print("Enter new first name/phone number")
    new_value = input()
    update_contact(last_name, attribute, new_value)

while True:
    print("Want to delete some data? yes/no")
    mode = input()
    if mode == "no":
        break
    cur.execute("""SELECT * FROM Contacts""")
    print(cur.fetchall())
    print("Enter last name")
    last_name = input()
    delete_contact(last_name)

connection.commit()
cur.close()
connection.close()
