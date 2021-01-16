import unittest
import MathFunctions


class KnownValues(unittest.TestCase):
	#Test areaCircle()
	def test_areaCircle_for_10radius(self):
		#Capture the results of the function
		result = MathFunctions.areaCircle(10)
		#Check for expected output
		expected = 314.1592653589793
		self.assertEqual(expected, result)

	def test_areaCircle_for_2radius(self):
		#Capture the results of the function
		result = MathFunctions.areaCircle(2)
		#Check for expected output
		expected = 12.566370614359172
		self.assertEqual(expected, result)


#Run the tests
if __name__  == '__main__':
	unittest.main()