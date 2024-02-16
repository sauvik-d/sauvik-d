class Fraction:
    def __int__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __lt__(self, other):
        left = self.numerator / self.denominator
        right = other.numerator / other.denominator
        return left < right

    def __mul__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

