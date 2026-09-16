import sqlite3
con = sqlite3.connect("bank.db")

cursor = con.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("""CREATE TABLE IF NOT EXISTS users
                  (
                      id        INTEGER PRIMARY KEY AUTOINCREMENT,
                      name      VARCHAR(20)        NOT NULL,
                      surname   VARCHAR(30)        NOT NULL,
                      email     VARCHAR(50) UNIQUE NOT NULL,
                      phone_num VARCHAR(12) UNIQUE NOT NULL
                  )""")

cursor.execute("DROP TABLE IF EXISTS accounts")
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts
                  (
                      id      INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_id INTEGER        NOT NULL,
                      amount  DECIMAL(20, 2) NOT NULL,
                      FOREIGN KEY (user_id) REFERENCES users (id)
                  )
""")

cursor.execute("DROP TABLE IF EXISTS transactions")
cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        amount DECIMAL(10, 2) NOT NULL,
                                        from_account_id INTEGER NOT NULL,
                                        to_account_id INTEGER NOT NULL,
                                        date TEXT NOT NULL,
    
                                        FOREIGN KEY (from_account_id) REFERENCES accounts(id),
                                        FOREIGN KEY (to_account_id) REFERENCES accounts(id)
                  )""")

cursor.execute("DROP TABLE IF EXISTS credentials")
cursor.execute("""CREATE TABLE IF NOT EXISTS credentials
                  (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      login VARCHAR(50) UNIQUE NOT NULL,
                      password TEXT NOT NULL,
                      user_id INTEGER NOT NULL,
                      
                      FOREIGN KEY (user_id) REFERENCES users(id)

                  )""")

# Funkcje
def add_user(name, surname, email, phone_num):
    cursor.execute("""INSERT INTO users(name, surname, email, phone_num) VALUES (?, ?, ?, ?)""",[name, surname, email, phone_num])
    con.commit()

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
            name, surname, email, phone_num = input("Imie: "), input("Nazwisko: "), input("E-Mail: "), input("Numer tel.: ")
            add_user(name, surname, email, phone_num)
            break
        case "3":
            is_finished = True
            break
        case default:
            print("Niepoprawny wybór")
