from random import randint
import hashlib
import hmac

from ECC.Math.field_element import FieldElement
from ECC.Math.point import Point


A = 0
B = 7
P = 2**256 - 2**32 - 977
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class S256Field(FieldElement):

    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=P)

    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)


class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)

        else:
            super().__init__(x=x, y=y, a=a, b=b)

    def __repr__(self):
        if self.x is None:
            return 'S256Point(infinity)'
        else:
            return f'S256Point({self.x}, {self.y})'

    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)

    def verify(self, z, sig):
        sig_inv = pow(sig.s, N-2, N)
        u = (z * sig_inv) % N
        v = (sig.r * sig_inv) % N

        total = (u*G) + (v*self)
        return total.x.num == sig.r


G = S256Point(
    0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)


class Signature:
    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self):
        return f'Signature({self.r}, {self.s})'


class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G

    def hex(self):
        return '{}'.format(self.secret).zfill(64)

    def sign(self, z):
        k = self.deterministic_k(z)
        r = (k * G).x.num
        k_inv = pow(k, N-2, N)
        s = ((z + r * self.secret) * k_inv) % N
        if s > N/2:
            s = N - s
        return Signature(r, s)

    def deterministic_k(self, z):
        k = b'\x00' * 32
        v = b'\x00' * 32
        if z > N:
            z -= N

        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = hashlib.sha256

        k = hmac.new(k, v+b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v+b'\x01' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()

        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')

            if candidate >= 1 and candidate < N:
                return candidate
            k = hmac.new(k, v+b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()
