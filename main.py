import sqlite3

from functions import add, select
con=sqlite3.connect("bank.db")

# Główny program
is_finished = False

while not is_finished:
    print("1. Zaloguj się")
    print("2. Rejestracja")
    print("3. Wyjdź")

    selection = input("Wybór: ")
    match selection:
        case "1":
            ...
            break
        case "2":
            name, surname, email, phone_num, login, password= input("Imie: "), input("Nazwisko: "), input("E-Mail: "), input(
                "Numer tel.: "), input("login:") , input("password: ")
            add(con=con,table_name='users', name=name, surname=surname, email=email, phone_num=phone_num)
            user = select(con=con, table_name="users", email=email).fetchone()
            add(con=con, table_name="credentials", login=login, password=password, user_id=user[0])
            break
        case "3":
            is_finished = True
            break
        case default:
            print("Niepoprawny wybór")