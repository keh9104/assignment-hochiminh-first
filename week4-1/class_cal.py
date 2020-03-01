class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def subtract(self):
        calculate.subtract = self.first - self.second
        return self.subtract

    def add(self):
        calculate.add = self.first + self.second
        return self.add

    def multiplication(self):
        calculate.multiplication = self.first * self.second
        return self.multiplication

    def division(self):
        calculate.division = self.first / self.second
        return self.division


calculate = Calculator(5, 9)
print(calculate.subtract())
print(calculate.add())
print(calculate.multiplication())
print(calculate.division())
