class Calculator:
    def __init__(self, a: int, b: int):
        self.first_number = a
        self.second_number = b

    def summa(self):
        return self.first_number + self.second_number

    def minus(self, first_to_second=True):
        if first_to_second:
            return self.first_number - self.second_number
        return self.second_number - self.first_number