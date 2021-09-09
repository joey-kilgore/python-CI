import unittest
from calculator import add

class TestCalc(unittest.TestCase):
	def test_pos(self):
		result = add(1,2)
		self.assertEqual(result,3)

	def test_neg(self):
		result = add(-1,-2)
		self.assertEqual(result,-3)
