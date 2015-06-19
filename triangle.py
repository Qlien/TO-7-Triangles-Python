import unittest

def isValid( a, b, c ):
	if ((a + b <= c) or (b + c <= a) or (c + a <= b) or a < 0 or	b < 0 or c < 0):
		return 0
	else:
		return 1

def triangleType( a, b, c ):
	if (isValid( a, b, c ) == 0):
		return 0
	elif (a == b and b == c):
		return 2
	elif ((a == b and b != c) or (a == c and a != b) or (c == b and b != a)):
		return 3
	elif ((a != b and b != c and c != a)):
		return 4
	else:
		return 0
		
class TestStringMethods(unittest.TestCase):
	def test_isValid1(self):
		self.assertEqual(isValid( 2, 2, 2 ), 1)
			
	def test_isValid2(self):
		self.assertEqual(isValid( -2, 2, 2 ), 0)

	def test_isEquilateral1(self):
		self.assertEqual(triangleType( 5, 5, 5 ), 2)

	def test_isIsosceles1(self):
		self.assertEqual(triangleType( 4, 4, 6 ), 3)
		
	def test_isScalene1(self):
		self.assertEqual(triangleType( 3, 4, 5 ), 4)
		
if __name__ == '__main__':
	unittest.main()