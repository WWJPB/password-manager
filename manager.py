import mysql.connector
import colorama
import sys
import os
import random

connection = mysql.connector.connect( 
    host = '127.0.0.1', 
    user = 'root',
    password = '',
    database = 'password_manager', 
    )

cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
database_exists = False
for db in databases:
    if "password_manager" in db:
        database_exists = True
        break

if not database_exists:
    query1 = "CREATE DATABASE password_manager"
    cursor.execute(query1)
    print("Database created")

cursor.execute("USE password_manager")

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
table_exists = False
for tbl in tables:
    if "passwords" in tbl:
        table_exists = True
        break

if not table_exists:
    query2 = "CREATE TABLE passwords(id int NOT NULL AUTO_INCREMENT, przeznaczenie varchar(30), HASLO varchar(30), PRIMARY KEY (id))"
    cursor.execute(query2)
    print("Table created")

connection.commit()

colorama.init(autoreset=True)

class Passwords:
    def generate_password(self):
        lower_case = "abcdefghijklmnqprstwvxyz"
        upper_case = "ABCDEFGHIJKLMNQPRSTVWXYZ"
        number = "1234567890"
        symbols = "!@#$%^&*><+-"
        Use_for = lower_case + upper_case + number + symbols
        lenght_for_pass = 8
        password = "".join(random.sample(Use_for, lenght_for_pass))
        print("password:", password)
    def add_password(self):
        password = input("Input password: \n")
        name = input("Password purpose: ")
        query = 'INSERT INTO passwords(przeznaczenie, HASLO) VALUES(%s, %s)'
        cursor = connection.cursor()
        cursor.execute(query, (name, password))
        connection.commit()
        print("password added")
    def update_password(self):
        purpose = input("Input password purpose: \n")
        password = input("Input new password: \n")
        update = 'UPDATE passwords SET HASLO = %s WHERE przeznaczenie = %s'
        cursor = connection.cursor()
        cursor.execute(update, (password, purpose))
        connection.commit()
        print("Password updated")
    def delete_password(self):
        purpose = input("Input password purpose: \n")
        delete = 'DELETE FROM passwords WHERE przeznaczenie = %s'
        cursor = connection.cursor()
        cursor.execute(delete, (purpose,))
        connection.commit()
        print("Password deleted")
    def show_password(self):
        cursor = connection.cursor()
        purpose = input("Input password purpose: \n")
        show = 'SELECT * FROM passwords WHERE przeznaczenie = %s'
        cursor.execute(show, (purpose,))
        result = cursor.fetchall()
        print(result)
    def all_passwords(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM passwords")
        result = cursor.fetchall()
        for i in result:
            print(i)

class generate(Passwords):
    pass
class add(Passwords):
    pass
class update(Passwords):
    pass
class delete(Passwords):
    pass
class show(Passwords):
    pass
class all(Passwords):
    pass

def exit():
    sys.Exit(0)

def clear():
    os.system('cls')

def menu():
    print(f"{colorama.Fore.WHITE}==========================================")
    print(f"{colorama.Fore.CYAN}password --generate  - generuje hasło\n")
    print(f"{colorama.Fore.CYAN}password --add  - dodaje hasło\n")
    print(f"{colorama.Fore.CYAN}password --update  - aktualizuje hasło\n")
    print(f"{colorama.Fore.CYAN}password --delete  - usuwa hasło\n")
    print(f"{colorama.Fore.CYAN}password --show  - pokazuje wybrane hasło\n")
    print(f"{colorama.Fore.CYAN}password --all  - pokazuje wszystkie hasła\n")
    print(f"{colorama.Fore.CYAN}clear  - czysci terminal\n")
    print(f"{colorama.Fore.CYAN}exit  - zamyka program\n")
    print("==========================================")

Generate = generate()
Add = add()
Update = update()
Delete = delete()
Show = show()
All = all()

print("Type help to open help menu\n")
print("")

while True:
    user = input(f"{colorama.Fore.MAGENTA}$")
    match user:
        case 'password --generate':
            Generate.generate_password()
        case 'password --add':
            Add.add_password()
        case 'password --update':
            Update.update_password()
        case 'password --delete':
            Delete.delete_password()
        case 'password --show':
            Show.show_password()
        case 'password --all':
            All.all_passwords()
        case 'exit':
            exit()
        case 'clear':
            clear()
        case 'help':
            menu()
        case _:
            print("Wprowadzona komenda nie istnieje\n")
        