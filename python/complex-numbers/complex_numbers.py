from math import cos, sin, exp


class ComplexNumber:
    def __init__(self, real, imaginary):
        """ Initialize a complex number :math:`x = a + i*b` with a real part :math:`a` and an imaginary part :math:`b`.

        :param real: The real part :math:`a` of a complex number :math:`x = a + i*b`.
        :param imaginary: The imaginary part :math:`b` of a complex number :math:`x = a + i*b`.
        """
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        """ Assert if two complex numbers are the same numbers.

        :param other: ComplexNumber - The second complex number in the assertion.
        :return: Boolean - True if both complex numbers are equal, False otherwise.
        """
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        """ Addition of two complex numbers.

        :param other: ComplexNumber - The second complex number in the addition.
        :return: ComplexNumber - Result of :math:`(a + i * b) + (c + i * d) = (a + c) + (b + d) * i`.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        """ Multiplication of two complex numbers.

        :param other: ComplexNumber - The second complex number in the multiplication.
        :return: ComplexNumber - Result of (a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i.
        """
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        """ Subtraction of two complex numbers.

        :param other: ComplexNumber - The right complex number in the subtraction.
        :return: ComplexNumber - Result of (a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i
        """
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        if self.imaginary != 0 and other.imaginary != 0:
            return ComplexNumber(
                (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2),
                (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2))
        else:
            return ComplexNumber(self.real/other.real, 0)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(exp(self.real) * cos(self.imaginary), exp(self.real) * sin(self.imaginary))
