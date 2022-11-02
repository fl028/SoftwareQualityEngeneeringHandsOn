import pytest
import webapp.db
from webapp.model_employee import employee

# unit testing with pytest lib
# run all tests: py -m pytest tests/pytest/
# run specific test: py -m pytest tests/pytest/test_db.py

@pytest.fixture
def setUp():
    print("setUp")
    db = webapp.db.DB()
    db.init_db()

def test_get_all_employees(setUp):
    #the unittest tests if three employee are in the database.

    # arrange
    db = webapp.db.DB()
    # act
    employees = db.get_all_employees()
    #assert
    assert len(employees) == 3

def test_raise_salary(setUp):
        # the unittest tests if the salary of the employee has increased

        # arrange
        db = webapp.db.DB()
        employees = db.get_all_employees()
        employee_juergen = employee(employees[1][0],employees[1][1],employees[1][2],employees[1][3],employees[1][4])
        # act
        employee_juergen_new_salary = employee_juergen.get_new_salary()
        print("old: " + str(employee_juergen.salary) + " new: " + str(employee_juergen_new_salary))
        #assert
        assert employee_juergen_new_salary > employee_juergen.salary

