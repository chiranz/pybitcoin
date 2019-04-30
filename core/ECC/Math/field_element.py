class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            raise ValueError(f' Num {num} not in field range 0 to {prime-1}')
        self.prime = prime
        self.num = num

    def __repr__(self):
        return f'FieldElement_{self.prime}({self.num})'

    def __eq__(self, other):
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if self.prime != other.prime:
            return TypeError(f'Cannot add two numbers in different fields.')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            return TypeError(f'Cannot substract two numbers in different fields.')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            return TypeError(f'Cannot multiply two numbers in different fields.')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime-1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
            # use Fermat's little theorem:
            # self.num**(p-1) % p == 1
            # this means:
            # 1/n == pow(n, p-2, p)
            # we return an element of the same class
        num = (self.num * pow(other.num, self.prime - 2,
                              self.prime)) % self.prime
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num, self.prime)
