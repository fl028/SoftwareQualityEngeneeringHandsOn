import unittest
import webapp.db
import sqlite3

# run tests: python -m unittest discover tests

class Testclass(unittest.TestCase):
    def setUp(self):
        print("setUp")
        webapp.db.init_db()

    def tearDown(self):
        print("tearDown")
        webapp.db.init_db()

    def test_get_all(self):
        db = sqlite3.connect('employees.db')
        cur = db.cursor()
        cur.execute("select * from employees")
        employees = cur.fetchall()

        self.assertEqual(len(employees), 3, "Should be 3")

if __name__ == '__main__':
    unittest.main()