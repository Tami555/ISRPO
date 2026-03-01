from calculator import Calculator
print("Hello world")

# calculator
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))

calc = Calculator(a, b)
print('Сумма: ', calc.summa())
print('Вычитание: ', calc.minus())