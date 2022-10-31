from screenplay.pattern import Actor, Task, Question
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from pages import EmployeePage


# Questions

class TextOf(Question):
    def __init__(self, by, query):
        self.by = by
        self.query = query

    def request_as(self, actor):
        browser: WebDriver = actor.using('browser')
        element = browser.find_element(self.by, self.query)
        text = element.get_attribute('innerHTML')
        return text.strip()

# Tasks

class Load(Task):
    def __init__(self, url):
        self.url = url

    def perform_as(self, actor):
        browser = actor.using('browser')
        browser.get(self.url)


class ClickOnButton(Task):
    def __init__(self,by, query):
        self.by = by
        self.query = query

    def perform_as(self, actor):
        browser = actor.using('browser')
        search_input = browser.find_element(self.by, self.query)
        search_input.click()


class VerifyResultEmployeeInfo(Task):
    def __init__(self, phrase):
        self.phrase = phrase.strip()

    def perform_as(self, actor):
        text = actor.asks_for(TextOf(*EmployeePage.EMPLOYEE_INFO))
        print(text + " --- " + self.phrase)
        assert text == self.phrase