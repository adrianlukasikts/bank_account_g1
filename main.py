from functions import add

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
            name, surname, email, phone_num = input("Imie: "), input("Nazwisko: "), input("E-Mail: "), input(
                "Numer tel.: ")
            add(table_name='users', name=name, surname=surname, email=email, phone_num=phone_num)
            break
        case "3":
            is_finished = True
            break
        case default:
            print("Niepoprawny wybór")