import unittest
import webapp.db

# run tests: python -m unittest discover tests

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

if __name__ == '__main__':
    unittest.main()