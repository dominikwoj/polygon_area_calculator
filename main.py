class Rectangle:
    width = 0
    height = 0
    def __init__(self):
        pass

    def set_width(self, w):
        self.width = w
    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.height * self.height

    def get_perimeter(self):
        return 2 * self.height * 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

class Square(Rectangle):
    pass