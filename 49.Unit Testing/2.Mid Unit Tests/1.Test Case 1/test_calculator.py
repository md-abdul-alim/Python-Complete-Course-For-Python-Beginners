import unittest
import calculator

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class TestCalculator(unittest.TestCase):

	# def test_add(self):
	# 	result = calculator.add(10,5)
	# 	# self.assertEqual(result, 14)
	# 	self.assertEqual(result, 15)
	##OR
	def test_add(self):
		self.assertEqual(calculator.add(10,5), 15)
		self.assertEqual(calculator.add(-1,1), 0)
		self.assertEqual(calculator.add(-1,-1), -2)

	def test_subtract(self):
		self.assertEqual(calculator.subtract(10,5), 5)
		self.assertEqual(calculator.subtract(-1,1), -2)
		self.assertEqual(calculator.subtract(-1,-1), 0)

	def test_multiply(self):
		self.assertEqual(calculator.multiply(10,5), 50)
		self.assertEqual(calculator.multiply(-1,1), -1)
		self.assertEqual(calculator.multiply(-1,-1), 1)

	def test_divide(self):
		self.assertEqual(calculator.divide(10,5), 2)
		self.assertEqual(calculator.divide(-1,1), -1)
		self.assertEqual(calculator.divide(-1,-1), 1)
		self.assertEqual(calculator.divide(5,2), 2.5)

		# self.assertRaises(ValueError, calculator.divide, 10,0)
		## OR Context method exception check
		#ei function dia amra amader code er exception error tik moto rise hosse kina seta check korbo
		with self.assertRaises(ValueError):
			calculator.divide(10,0)
			#calculator.divide(10,2)#this will show error








#Run the tests
if __name__  == '__main__':
	unittest.main()

#or run the command in console
#python -m unittest test_calculator.py