import random
try:
    print('Привет! Ты попал в числовую угадайку, тебе нужно угадать моё загаданное число')
    a, b = int(input('Введи нижний предел: ')), int(input('Введи верхний предел: '))
    x = random.randint(a, b)
    def is_valid(num):
        if a <= num <= b:
            return True
        else:
            return False
    def GuessTheNumber():
        while True:
            num = int(input())
            if is_valid(num):
                if num > x:
                    print(f'Неа, оно меньше {num}, попробуй еще раз')
                if num < x:
                    print(f'Неа, оно больше {num}, попробуй еще раз')
                if num == x:
                    print('Молодец! ты угадал число')
                    break
            else:
                print(f'А может быть все-таки введем целое число от {a} до {b}?')
    print('Введи число')
    GuessTheNumber()
except:
    print('Вводи только числа!')