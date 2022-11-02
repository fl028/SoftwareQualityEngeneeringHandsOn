import pytest
from screenplay.pattern import Actor
from interactions import *
from pages import IndexPage

# following: https://github.com/AutomationPanda/selenium-screenplay-python

# run all tests: py -m pytest tests/pytest/
# run specific test: py -m pytest tests/pytest/screenplay_pattern/test_gui.py

def test_gui(actor):
    #the unittest tests if three employee are displayed in the gui.

    # Arrange
    actor.attempts_to(Load(IndexPage.URL))

    # Act
    actor.attempts_to(ClickOnButton(*IndexPage.EMPLOYEE_BUTTON))

    # Assert
    actor.attempts_to(VerifyResultEmployeeInfo('There are 3 entries in the database.'))