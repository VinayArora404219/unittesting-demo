import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp1 = Employee('Corey', 'Schafer', 50000)
        self.emp2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')

        self.emp1.first = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.emp1.full_name, 'Corey Schafer')
        self.assertEqual(self.emp2.full_name, 'Sue Smith')

        self.emp1.first = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.full_name, 'John Schafer')
        self.assertEqual(self.emp2.full_name, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)


if __name__ == '__main__':
    unittest.main()


