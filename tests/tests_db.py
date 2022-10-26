import unittest
#import webapp.app
import sqlite3

# run tests: python -m unittest discover tests

class Testclass(unittest.TestCase):

    def test_get_all(self):
        db = sqlite3.connect('employees.db')
        cur = db.cursor()
        cur.execute("select * from employees")
        employees = cur.fetchall()

        self.assertEqual(len(employees), 3, "Should be 3")

if __name__ == '__main__':
    unittest.main()