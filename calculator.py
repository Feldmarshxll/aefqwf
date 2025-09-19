import math
try:
    one_digit = ['sqrt', 'log', 'log10', 'factorial', 'sin', 'cos', 'tan']
    two_digits = ['+', '-', '/', '*', 'pow', '//', '%', 'log(x, b)']
    not_zero_operations = ['/', '//', '%']
    operation = input('Введите математическую операцию(+, -, /, *, pow, //, %, sqrt, log, log10, log(x, b), factorial, sin, cos, tan): ')
    if operation in one_digit:
        n = eval(input('Введите число(ВВОДИТЬ ТОЛЬКО ЧИСЛО БЕЗ ВСЯКИХ КАВЫЧЕК): '))
        if operation == 'sqrt':
            print(f'Корень числа {n} равен {math.sqrt(n)}')
        elif operation == 'log':
            print(f'Логарифм числа {n} равен {math.log(n)}')
        elif operation == 'log10':
            print(f'Десятичный логарифм числа {n} равен {math.log10(n)}')
        elif operation == 'factorial':
            print(f'Факториал числа {n} равен {math.factorial(n)}')
        elif operation == 'sin':
            print(f'Синус числа {n} равен {math.sin(n)}')
        elif operation == 'cos':
            print(f'Косинус числа {n} равен {math.cos(n)}')
        elif operation == 'tan':
            print(f'Тангенс числа {n} равен {math.tan(n)}')
        else:
            print('КАК')
    elif operation in two_digits:
        a = eval(input('Введите первое число(ВВОДИТЬ ТОЛЬКО ЧИСЛО БЕЗ ВСЯКИХ КАВЫЧЕК): '))
        b = eval(input('Введите второе число(ВВОДИТЬ ТОЛЬКО ЧИСЛО БЕЗ ВСЯКИХ КАВЫЧЕК): '))
        if operation in not_zero_operations and b == 0:
            print('А по попе за деление на ноль?')
        else:
            if operation == '+':
                print(f'Сумма чисел {a} и {b} равна {a + b}')
            elif operation == '-':
                print(f'Разность чисел {a} и {b} равна {a - b}')
            elif operation == '/':
                print(f'Деление чисел {a} и {b} равна {a / b}')
            elif operation == '*':
                print(f'Число {a} умноженное на {b} равно {a * b}')
            elif operation == 'pow':
                print(f'Число {a} возведённое в степень {b} равно {math.pow(a, b)}, а число {b} возведённое в степень {a} равно {math.pow(b, a)}')
            elif operation == '//':
                print(f'Целочисленное деление числа {a} на число {b} равно {a // b}')
            elif operation == '%':
                print(f'Остаток от деления числа {a} на число {b} равно {a % b}')
            elif operation == 'log(x, b)':
                print(f'Логарифм числа {a} с основанием {b} равен {math.log(a, b)}')
            else:
                print('КАК')
    else:
        print('Ну ты конечно орех')
except:
    print('cazzo stai scherzando?')