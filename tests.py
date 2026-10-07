from unittest import TestCase
from main import add
from sqlite3 import Connection, connect

class AppTest(TestCase):
    con: Connection = connect()
    def test_setup(self):
        x = 2
        y = 3 + x
        z = x + y

        self.assertTrue(x == 2)
        self.assertTrue(y == 5)
        self.assertTrue(z == 7)
    #todo
    def test_add_user(self):
        add(table_name="users",name="janek",surname="perlowski",email="1@gmail.com",phone_num="112")
        user = self.con.cursor().execute("SELECT * FROM users WHERE name='janek'").fetchmany()
        self.assertTrue(len(user)>0)