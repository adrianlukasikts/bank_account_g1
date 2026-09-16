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
                                        from_uid INTEGER NOT NULL,
                                        to_uid INTEGER NOT NULL,
                                        date TEXT NOT NULL,
    
                                        FOREIGN KEY (from_uid) REFERENCES users(id),
                                        FOREIGN KEY (to_uid) REFERENCES users(id)
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
