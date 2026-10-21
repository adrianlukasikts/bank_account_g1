from unittest import TestCase
from functions import add, select
from sqlite3 import Connection, connect

class AppTest(TestCase):
    con: Connection = connect("bank.db")
    def test_add_user(self):
        add(con=self.con,table_name="users",name="janek",surname="perlowski",email="1@gmail.com",phone_num="112")
        user = select(con=self.con, table_name="users", email="1@gmail.com").fetchmany()
        self.assertTrue(len(user)>0)