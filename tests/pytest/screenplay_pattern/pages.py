from selenium.webdriver.common.by import By

class IndexPage:
    URL = 'http://127.0.0.1:5000/'
    EMPLOYEE_BUTTON = (By.ID, "employees_button")

class EmployeePage:
    EMPLOYEE_BUTTON_CREATE = None
    EMPLOYEE_TABLE = None
    EMPLOYEE_INFO = (By.ID, "info")