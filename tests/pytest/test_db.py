import webapp.db
import pytest
from webapp.model_employee import employee

# unit testing with pytest lib
# run tests: python -m pytest tests/pytest/

@pytest.fixture
def setUp():
    print("setUp")
    db = webapp.db.DB()
    db.init_db()

def test_get_all_employees(setUp):
    # arrange
    db = webapp.db.DB()
    # act
    employees = db.get_all_employees()
    #assert
    assert len(employees) == 3

def test_raise_salary(setUp):
        # arrange
        db = webapp.db.DB()
        employees = db.get_all_employees()
        employee_juergen = employee(employees[1][0],employees[1][1],employees[1][2],employees[1][3],employees[1][4])
        # act
        new_salary = employee_juergen.get_new_salary()
        #assert
        assert new_salary == 26000

