class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def info(self):
        print(f"{self.width} × {self.height}: площа = {self.area()}, периметр = {self.perimeter()}")


r1 = Rectangle(5, 3)
r2 = Rectangle(10, 4)

r1.info()
r2.info()
