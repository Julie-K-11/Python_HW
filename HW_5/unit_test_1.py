import unittest

print("-------------Завдання 1-------------\n")

class MathOperation:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_elements(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)
    
class UtilsTestCase(unittest.TestCase):

    def setUp(self):
        self.value = MathOperation([9, 2, 0, 4, 3])

    def test_sum_elements(self):
        self.assertEqual(self.value.sum_elements(), 18)

    def test_average(self):
        self.assertEqual(self.value.average(), 3.6)

    def test_maximum(self):
        self.assertEqual(self.value.maximum(), 9)

    def test_minimum(self):
        self.assertEqual(self.value.minimum(), 0)

if __name__ == '__main__':
    unittest.main()