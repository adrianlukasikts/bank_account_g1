import sqlite3
con = sqlite3.connect("bank.db")

cursor = con.cursor()
'''
cursor.execute("""CREATE TABLE users(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name VARCHAR(20) NOT NULL,
                                        surname VARCHAR(30) NOT NULL,
                                        email VARCHAR(50) UNIQUE NOT NULL,
                                        phone_num VARCHAR(12) UNIQUE NOT NULL
                  )""")
'''

'''
cursor.execute("""CREATE TABLE transactions(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        amount DECIMAL(10, 2) NOT NULL,
                                        from_uid INTEGER NOT NULL,
                                        to_uid INTEGER NOT NULL,
                                        date TEXT NOT NULL,
    
                                        FOREIGN KEY (from_uid) REFERENCES users(id),
                                        FOREIGN KEY (to_uid) REFERENCES users(id)
                  )""")
'''