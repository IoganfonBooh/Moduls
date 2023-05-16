class NonPositiveDigitException(ValueError):
    pass
class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')
        self.a = a
    def get_area_square(self):
        return self.a**2
square_1 = Square(0)
print(square_1.get_area_square())