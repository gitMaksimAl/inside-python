from io import StringIO
import unittest
from unittest.mock import patch

from task3 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp = Employee('Ivanov', 'Ivan', 'Ivanovich',
                            30, 'manager', 55_000)

    def test_employee_full_name(self):
        self.assertEqual(self.emp.full_name(), 'Ivanov Ivan Ivanovich')

    def test_employee_birthday(self):
        self.emp.birthday()
        self.assertEqual(self.emp.get_age(), 31)

    def test_employee_raise_salary(self):
        self.emp.raise_salary(10)
        self.assertEqual(55_000.0, self.emp.salary)

    @patch('sys.stdout', new_callable=StringIO)
    def test_employee_str(self, mock_stdout):
        print(self.emp)
        self.assertEqual('Ivanov Ivan Ivanovich (Manager)\n',
                         mock_stdout.getvalue())
        
    def test_employee_last_name_title(self):
        self.assertNotEqual('Ivan', self.emp.last_name)
