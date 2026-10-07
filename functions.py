from sqlite3 import Connection

from pygments.lexers import sql


def add(con: Connection, table_name: str, **params):
    con.cursor().execute(
        f"INSERT INTO {table_name}({", ".join(params.keys())}) VALUES ({", ".join(['?'] * len(params))})",
        list(params.values()))
    con.commit()

def select(con: Connection, table_name: str, **params):
    # obj = {"name": "kuba", "surname": "wilk", "year": "2010"}
    #
    # l = []
    #
    # for k, v in obj.items():
    #     l.append(f"{k} = ?")
    #
    # print(" AND ".join(l))

    con.cursor().execute(
        f"SELECT * FROM {table_name} WHERE {="?"}"
    )