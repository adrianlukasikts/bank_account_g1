import sqlite3

from functions import add_user, select, add

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
            login, password= input("login: "), input("password: ")
            result = select(con=con, table_name="credentials", selectors=["user_id"], login=login, password=password)
            if not result:
                print("Niepoprawne dane logowania")
            else:
                id = result[0][0]

                result = select(con=con, table_name="users", selectors=["id", "name", "surname"], id=id)

                if result:
                    result = result[0]
                else:
                    print("User not found")

                print(f"Zalogowano na użytkownika {result[1]} {result[2]}")

                result = select(con=con, table_name="accounts", selectors=["id", "user_id", "amount"], user_id=id)
                print(result)


                #todo zdecydowanie do poprawy

                user_id = id
                while True:
                    print("1. Utwórz konto" )
                    print("2. Wyświetl stan kont")
                    print("3. Wpłata na konto")
                    print("4. Wykonaj przelew")


                    selection = input("Wybór: ")
                    match selection:
                        case "1":
                            add(con, "accounts", user_id=user_id, amount=0)
            break
        case "2":
            name, surname, email, phone_num, login, password= input("Imie: "), input("Nazwisko: "), input("E-Mail: "), input(
                "Numer tel: "), input("login:") , input("password: ")
            add_user(con=con,name=name,surname=surname,email=email,phone_num=phone_num,login=login,password=password)
            break
        case "3":
            is_finished = True
            break
        case default:
            print("Niepoprawny wybór")