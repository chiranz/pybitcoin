from unittest import TestCase


class Point:
    def __init__(self, x, y, a, b):

        self.x = x
        self.y = y
        self.a = a
        self.b = b
        if self.x is None and self.y is None:
            return

        if self.y**2 != self.x**3 + self.a * self.x + self.b:
            raise ValueError(f'({self.x}, {self.y}) is not on the curve')

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        return f'Point({self.x}, {self.y})_{self.a}_{self.b}'

    def __add__(self, other):

        if self.a != other.a or self.b != other.b:
            raise TypeError(
                f'Points {self}, {other} are not on the same curve.')

        # IF OTHER IS AT INFINITY
        if other is None:
            return self

        # IF SELF IS AT INFINITY
        if self is None:
            return other

        # When the point opposite to X axis but equal
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        # When the point is vertical and is at y == 0
        if self.x == other.x and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

        # When the points are different
        if self.x != other.x:
            # s is slope here
            s = other.y-self.y/other.x-self.x
            x = s**2 - self.x - other.x
            y = s(x-self.x) + self.y
            return self.__class__(x, y, self.a, self.b)

        # When the point is tangent to the curve.
        if self == other:
            # slope of elliptic curve d/dx(y**2)
            # = d/dx(x**3+ax+b) => dy/dx = (3x**2 + a)/2y
            s = (3 * self.x**2 + self.a)/2*self.y
            x = s**2 - 2 * self.x
            y = s(x-self.x) + self.y
            return self.__class__(x, y, self.a, self.b)
