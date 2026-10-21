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
