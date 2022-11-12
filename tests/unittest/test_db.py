import unittest
from unittest.mock import Mock, patch
import webapp.db
from webapp.model_employee import employee

# unit testing with default unittest lib by python
# run all tests: py -m unittest discover tests/unittest
# run specific: py -m unittest tests/unittest/test_db.py

class TestDatabase(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")
        db = webapp.db.DB()
        db.init_db()

    def tearDown(self):
        print("tearDown\n")

    def test_get_all_employees(self):
        #the unittest tests if three employee are in the database.

        # arrange
        db = webapp.db.DB()
        # act
        employees = db.get_all_employees()
        print("len: " + str(len(employees)))
        #assert
        self.assertEqual(len(employees), 3, "Should be 3")

    def get_all_employees_mock(*args, **kwargs):
        print('Mock DB call')
        mock_employees = { "data": [[1,"Maxi","Mueller",100000,"Development"]]}
        return mock_employees

    @patch('webapp.db.DB.get_all_employees', side_effect=get_all_employees_mock)
    def test_get_all_employees_mock(self, employees_mock):
        #the unittest tests if an employee is in the database. The output of the employees is mocked.

        # arrange
        db = webapp.db.DB()
        # act
        employees = db.get_all_employees()
        #assert
        self.assertEqual(len(employees), 1, "Should be 1")

    def test_raise_salary(self):
        # the unittest tests if the salary of the employee has increased

        # arrange
        db = webapp.db.DB()
        employees = db.get_all_employees()
        employee_juergen = employee(employees[1][0],employees[1][1],employees[1][2],employees[1][3],employees[1][4])
        # act
        employee_juergen_new_salary = employee_juergen.get_new_salary()
        print("old: " + str(employee_juergen.salary) + " new: " + str(employee_juergen_new_salary))
        #assert
        self.assertGreater(employee_juergen_new_salary,employee_juergen.salary, "new salary should be bigger")

    def test_employee_model(self):
        #TODO: Aufgabe 1
        pass

if __name__ == '__main__':
    unittest.main()