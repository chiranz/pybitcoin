from Point_and_FieldElement.field_element import FieldElement, Point


A = 0
B = 7
P = 2**256 - 2**32 - 977
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class S256Field(FieldElement):
	def __init__(self, num=num, prime=None):
		super().__init__(num=num, prime=P)

	def __repr__(self):
		return '{:x}'.format(self.num).zfill(64)


class S256Point(Point):
	def __init__(self, x, y, a=None, b=None):
		a, b = S256Field(A), S256Field(B)
		if type(x) == int:
			super().__init__(x=S256Field(x), y=S256Field(y), a=A, b=B)

		else:
			super().__init__(x=x,y=y,a,b)

	def __repr__(self):
		if self.x is None:
			return 'S256Point(infinity)'
		else:
			return f'S256Point({self.x}, {self.y})'


	def __rmul__(self, coefficient):
		coef = coefficient % N
		return super().__rmul__(coef)

		
G = S256Point(
    0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)

		