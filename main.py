class Rectangle:
    width = 0
    height = 0

    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        return 'Too big for picture.' \
            if self.width > 50 or self.height > 50 \
            else '\n'.join(['*' * self.width for i in range(self.height)])

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self):
        super.__init__()


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())
#
# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))