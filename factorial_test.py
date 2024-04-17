import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_1(self):
        result = factorial(1)
        self.assertEqual(result,1)

    def test_2(self):
        result = factorial(2)
        self.assertEqual(result,2)

    def test_3(self):
        result = factorial(3)
        self.assertEqual(result,6)

    def test_4(self):
        result = factorial(4)
        self.assertEqual(result,24)

    def test_5(self):
        result = factorial(5)
        self.assertEqual(result,120)

    def test_6(self):
        result = factorial(6)
        self.assertEqual(result,720)

    def test_7(self):
        result = factorial(7)
        self.assertEqual(result,5040)

    def test_8(self):
        result = factorial(8)
        self.assertEqual(result,40320)

    def test_9(self):
        result = factorial(9)
        self.assertEqual(result,362880)

    def test_0(self):
        result = factorial(0)
        self.assertEqual(result,1)

if __name__ == "__main__":
    unittest.main()