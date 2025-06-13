import unittest

print("-------------Завдання 2-------------\n")

class Number:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def to_binary(self):
        return bin(self.value)

    def to_octal(self):
        return oct(self.value)

    def to_hex(self):
        return hex(self.value)

class UtilsTestCase(unittest.TestCase):

    def setUp(self):
        self.number = Number(18)

    def test_get_value(self):
        self.assertEqual(self.number.get_value(), 18)

    def test_set_value(self):
        self.number.set_value(34)
        self.assertEqual(self.number.get_value(), 34)

    def test_to_binary(self):
        self.assertEqual(self.number.to_binary(), '0b10010')

    def test_to_octal(self):
        self.assertEqual(self.number.to_octal(), '0o22')

    def test_to_hex(self):
        self.assertEqual(self.number.to_hex(), '0x12')

if __name__ == '__main__':
    unittest.main()
