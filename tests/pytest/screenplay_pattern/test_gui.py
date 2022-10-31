import pytest
from screenplay.pattern import Actor
from interactions import *
from pages import IndexPage

# following: https://github.com/AutomationPanda/selenium-screenplay-python

def test_gui(actor):
    # Arrange
    actor.attempts_to(Load(IndexPage.URL))

    # Act
    actor.attempts_to(ClickOnButton(*IndexPage.EMPLOYEE_BUTTON))

    # Assert
    actor.attempts_to(VerifyResultEmployeeInfo('There are 3 entries in the database.'))