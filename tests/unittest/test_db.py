import unittest
from unittest.mock import Mock
import webapp.db
from webapp.model_employee import employee

# unit testing with default unittest lib by python
# run tests: python -m unittest discover tests/unittest

class TestDatabase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        db = webapp.db.DB()
        db.init_db()

    def tearDown(self):
        print("tearDown")
        db = webapp.db.DB()
        db.init_db()

    def test_get_all_employees(self):
        # arrange
        db = webapp.db.DB()
        # act
        employees = db.get_all_employees()
        #assert
        self.assertEqual(len(employees), 3, "Should be 3")

    def test_raise_salary(self):
        # arrange
        db = webapp.db.DB()
        employees = db.get_all_employees()
        employee_juergen = employee(employees[1][0],employees[1][1],employees[1][2],employees[1][3],employees[1][4])
        employee_juergen.get_new_salary = Mock(return_value=28000)
        # act
        new_salary = employee_juergen.get_new_salary()
        #assert
        self.assertEqual(new_salary, 28000, "Should be 28k")


if __name__ == '__main__':
    unittest.main()