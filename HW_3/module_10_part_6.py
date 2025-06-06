print("------------Завдання 1-2------------\n")

import math

class Figure:
    def area(self):
        return 0

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return "Figure"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle area = {self.area()}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle area = {self.area()}"

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Right Triangle area = {self.area()}"

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Trapezoid area = {self.area()}"

figures = [
    Rectangle(4, 5),
    Circle(3),
    RightTriangle(3, 4),
    Trapezoid(3, 5, 4)
]

for f in figures:
    print(str(f))
    print("int(area) =", int(f))
    print()


print("\n-------------Завдання 3-------------\n")

class Shape:
    def Show(self):
        print("Shape")

    def Save(self, file):
        file.write("Shape\n")

    def Load(self, lines):
        return

class Square(Shape):
    def __init__(self, x=0, y=0, side=0):
        self.x = x
        self.y = y
        self.side = side

    def Show(self):
        print(f"Square: Top-left=({self.x}, {self.y}), Side={self.side}")

    def Save(self, file):
        file.write("Square\n")
        file.write(f"{self.x} {self.y} {self.side}\n")

    def Load(self, line):
        self.x, self.y, self.side = map(int, line.strip().split())

class Rectangle(Shape):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def Show(self):
        print(f"Rectangle: Top-left=({self.x}, {self.y}), Width={self.w}, Height={self.h}")

    def Save(self, file):
        file.write("Rectangle\n")
        file.write(f"{self.x} {self.y} {self.w} {self.h}\n")

    def Load(self, line):
        self.x, self.y, self.w, self.h = map(int, line.strip().split())

class Circle(Shape):
    def __init__(self, cx=0, cy=0, r=0):
        self.cx = cx
        self.cy = cy
        self.r = r

    def Show(self):
        print(f"Circle: Center=({self.cx}, {self.cy}), Radius={self.r}")

    def Save(self, file):
        file.write("Circle\n")
        file.write(f"{self.cx} {self.cy} {self.r}\n")

    def Load(self, line):
        self.cx, self.cy, self.r = map(int, line.strip().split())

class Ellipse(Shape):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def Show(self):
        print(f"Ellipse: Top-Left=({self.x}, {self.y}), Width={self.w}, Height={self.h}")

    def Save(self, file):
        file.write("Ellipse\n")
        file.write(f"{self.x} {self.y} {self.w} {self.h}\n")

    def Load(self, line):
        self.x, self.y, self.w, self.h = map(int, line.strip().split())

def save_shapes(shapes, filename):
    with open(filename, "w") as f:
        for shape in shapes:
            shape.Save(f)

def load_shapes(filename):
    shapes = []
    with open(filename, "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            shape_type = lines[i].strip()
            data_line = lines[i + 1]
            i += 2

            if shape_type == "Square":
                shape = Square()
            elif shape_type == "Rectangle":
                shape = Rectangle()
            elif shape_type == "Circle":
                shape = Circle()
            elif shape_type == "Ellipse":
                shape = Ellipse()
            else:
                shape = Shape()

            shape.Load(data_line)
            shapes.append(shape)
    return shapes

shapes = [
    Square(1, 2, 4),
    Rectangle(3, 5, 6, 2),
    Circle(10, 8, 5),
    Ellipse(0, 0, 7, 3)
]

save_shapes(shapes, "shapes.txt")

print("Загружені фігури")
loaded = load_shapes("shapes.txt")
for shape in loaded:
    shape.Show()