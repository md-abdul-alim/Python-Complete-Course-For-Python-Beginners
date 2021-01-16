import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("setUpClass\n")

	@classmethod
	def tearDownClass(cls):
		print("tearDownClass")

	def setUp(self):
		print("setUp")
		
		self.emp_1 = Employee('Abdul','Alim', 50000)
		self.emp_2 = Employee('Kawsar','Abdullah', 70000)

	def tearDown(self):
		print("tearDown\n")
		
	def test_email(self):
		print("Test Email")

		self.assertEqual(self.emp_1.email, 'Abdul.Alim@email.com')
		self.assertEqual(self.emp_2.email, 'Kawsar.Abdullah@email.com')

		self.emp_1.first = 'Asha'
		self.emp_2.first = 'Alamgir'

		self.assertEqual(self.emp_1.email, 'Asha.Alim@email.com')
		self.assertEqual(self.emp_2.email, 'Alamgir.Abdullah@email.com')

	def test_fullname(self):
		print("Test Fullname")

		self.assertEqual(self.emp_1.fullname, 'Abdul Alim')
		self.assertEqual(self.emp_2.fullname, 'Kawsar Abdullah')

		self.emp_1.first = 'Asha'
		self.emp_2.first = 'Alamgir'

		self.assertEqual(self.emp_1.fullname, 'Asha Alim')
		self.assertEqual(self.emp_2.fullname, 'Alamgir Abdullah')

	def test_apply_raise(self):
		print("Test Apply Raise")

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 50000)
		self.assertEqual(self.emp_2.pay, 70000)

if __name__ == '__main__':
	unittest.main()

