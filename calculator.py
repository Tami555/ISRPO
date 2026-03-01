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

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self, first_to_second=True):
        zero_string = "Ошибка: Делимое число не может быть нулем"
        if first_to_second:
            return self.first_number / self.second_number if self.second_number else zero_string
        return self.second_number / self.first_number if self.first_number else zero_string
