print("-------------Завдання 1-------------\n")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return 2 * 3.1416 * self.radius < 2 * 3.1416 * other.radius

    def __le__(self, other):
        return not (self > other)

    def __gt__(self, other):
        return 2 * 3.1416 * self.radius > 2 * 3.1416 * other.radius

    def __ge__(self, other):
        return not (self < other)

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def __str__(self):
        return f"Circle radius: {self.radius}"

print("\n-------------Завдання 2-------------\n")

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

print("\n-------------Завдання 3-------------\n")

class Airplane:
    def __init__(self, type_name, passengers, max_passengers):
        self.type_name = type_name
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __eq__(self, other):
        return self.type_name == other.type_name

    def __add__(self, num):
        return Airplane(self.type_name, self.passengers + num, self.max_passengers)

    def __sub__(self, num):
        return Airplane(self.type_name, self.passengers - num, self.max_passengers)

    def __iadd__(self, num):
        self.passengers += num
        if self.passengers > self.max_passengers:
            self.passengers = self.max_passengers
        return self

    def __isub__(self, num):
        self.passengers -= num
        if self.passengers < 0:
            self.passengers = 0
        return self

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return not (self > other)

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return not (self < other)

    def __str__(self):
        return f"Airplane: {self.type_name}, Passengers: {self.passengers}/{self.max_passengers}"

print("\n-------------Завдання 4-------------\n")

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return not (self > other)

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return not (self < other)

    def __str__(self):
        return f"Flat: Area={self.area}, Price={self.price}"