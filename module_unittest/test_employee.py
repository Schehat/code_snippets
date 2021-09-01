import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    # starts before everything
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    # starts after everything
    @classmethod
    def tearDownClass(cls):
        print("teardownClass")

    # starts before every test
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    # starts after every test
    def tearDown(self):
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # mocking: if a test has other dependencies we can simulate it
    # and check if the method works regardless of wheather the dependencies
    # are working correctly. E.g. a request so a website which is currently down
    def test_monthly_schedule(self):
        # argument: in class Employee in the monthly_scheduled method
        # is the command request.get which has the dependency wheather the
        # website is currently online
        # Note: without paranthesis
        with patch("employee.requests.get") as mocked_get:
            # simulate True value
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            # mocked object remembers what they called and with what values
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            # simulated False value
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
