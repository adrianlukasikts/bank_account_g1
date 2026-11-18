from sqlite3 import Connection, Cursor

from pygments.lexers import sql


def add(con: Connection, table_name: str, **params):
    con.cursor().execute(
        f"INSERT INTO {table_name}({", ".join(params.keys())}) VALUES ({", ".join(['?'] * len(params))})",
        list(params.values()))
    con.commit()

def select(con: Connection, table_name: str, **params) -> Cursor:
    return con.cursor().execute(
        f'SELECT * FROM {table_name} WHERE {" AND ".join([f"{k} = ?" for k in params])}',
        list(params.values())
    )
class UserAlreadyExists(Exception):
    pass
def add_user(con:Connection, name:str, surname:str, email:str, phone_num:str,login:str, password:str):
    try:
        add(con=con, table_name='users', name=name, surname=surname, email=email, phone_num=phone_num)
        user = select(con=con, table_name="users", email=email).fetchone()
        add(con=con, table_name="credentials", login=login, password=password, user_id=user[0])
        #todo rzucanie wyjatku UserAlreadyExists
    except UserAlreadyExists:
        print("Użytkownik już istnieje")
        con.cursor().execute("ROLLBACK")


