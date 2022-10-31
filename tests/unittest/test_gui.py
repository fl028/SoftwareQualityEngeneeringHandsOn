import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


# unit testing with default unittest lib by python
# run tests: python -m unittest discover tests/unittest

class TestDatabase(unittest.TestCase):
  driver = None

  def setUp(self):
      print("\nsetUp")
      self.driver = webdriver.Chrome(ChromeDriverManager().install())

  def tearDown(self):
      print("tearDown\n")
      self.driver.quit()

  def test_gui(self):
      #arrange
      self.driver.get("http://127.0.0.1:5000/")
      print(self.driver.title)
      self.driver.maximize_window()
      time.sleep(1)

      #act
      button_search = self.driver.find_element(By.ID, "employees_button")
      button_search.click()
      time.sleep(1)
      info_search = self.driver.find_element(By.ID, "info")
      print(info_search.text)

      #assert
      self.assertEqual(info_search.text,'There are 3 entries in the database.', 'Message not displayed correct.')

if __name__ == '__main__':
    unittest.main()