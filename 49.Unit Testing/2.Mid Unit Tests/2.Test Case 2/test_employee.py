import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def test_email(self):
		emp_1 = Employee('Abdul','Alim', 50000)
		emp_2 = Employee('Kawsar','Abdullah', 70000)

		self.assertEqual(emp_1.email, 'Abdul.Alim@email.com')
		self.assertEqual(emp_2.email, 'Kawsar.Abdullah@email.com')

		emp_1.first = 'Asha'
		emp_2.first = 'Alamgir'

		self.assertEqual(emp_1.email, 'Asha.Alim@email.com')
		self.assertEqual(emp_2.email, 'Alamgir.Abdullah@email.com')

	def test_fullname(self):
		emp_1 = Employee('Abdul','Alim', 50000)
		emp_2 = Employee('Kawsar','Abdullah', 70000)

		self.assertEqual(emp_1.fullname, 'Abdul Alim')
		self.assertEqual(emp_2.fullname, 'Kawsar Abdullah')

		emp_1.first = 'Asha'
		emp_2.first = 'Alamgir'

		self.assertEqual(emp_1.fullname, 'Asha Alim')
		self.assertEqual(emp_2.fullname, 'Alamgir Abdullah')

	def test_apply_raise(self):
		emp_1 = Employee('Abdul','Alim', 50000)
		emp_2 = Employee('Kawsar','Abdullah', 70000)

		self.assertEqual(emp_1.fullname, 'Abdul Alim')
		self.assertEqual(emp_2.fullname, 'Kawsar Abdullah')

		emp_1.apply_raise()
		emp_2.apply_raise()

		self.assertEqual(emp_1.pay, 50000)
		self.assertEqual(emp_2.pay, 70000)

if __name__ == '__main__':
	unittest.main()