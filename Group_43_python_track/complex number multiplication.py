class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1.split('+'), num2.split('+')

        real1, imaginary1 = int(num1[0]), int(num1[1][:-1])
        real2, imaginary2 = int(num2[0]), int(num2[1][:-1])

        real = (real1 * real2) - (imaginary1 * imaginary2)
        imaginary = (real1 * imaginary2) + (real2 * imaginary1)

        return str(real) + '+' + str(imaginary) + 'i'
