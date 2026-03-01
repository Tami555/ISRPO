from calculator import Calculator
print("Hello world")

# calculator
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))

calc = Calculator(a, b)
print('Сумма: ', calc.summa())
print('Вычитание из 1-го 2-ое: ', calc.minus())
print('Вычитание из 2-го 1-ое: ', calc.minus(first_to_second=False))
print('Умножение: ', calc.multipart())
print('Деление: ', calc.delenie())