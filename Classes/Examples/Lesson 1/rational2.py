import math


class Rational:
    # class methods
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator,denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)

    def to_float(self):
        return self.numerator / self.denominator

    def multiply(self, other):
        return Rational(self.numerator*other.numerator, self.denominator*other.denominator)

    def divide(self, other):
        rec_other = Rational(other.denominator, other.numerator)
        return self.multiply(rec_other)


def main():
    x = Rational(3,4)
    y = Rational(1,5)
    quotient = x.divide(y)
    print( quotient )
    
    
if __name__ == "__main__":
    main()