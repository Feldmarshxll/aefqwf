import random

kolvo = int(input('Количество паролей для генерации:'))
len_parol = int(input('Длину паролей:'))
digit = '23456789' if input('Включать ли цифры:').lower() == 'да' else ''
big = 'ABCDEFGHIJKMNPQRSTUVWXYZ' if input('Включать ли прописные буквы:').lower() == 'да' else ''
small = 'abcdefghjklmnpqrstuvwxyz' if input('Включать ли строчные буквы').lower() == 'да' else ''
symvols = '!#$%&*+-=?@^_' if input('Включать ли символы !#$%&*+-=?@^_?').lower() == 'да' else ''
neformal = 'il1Lo0O' if input('Исключать ли неоднозначные символы il1Lo0O?').lower() == 'да' else ''
chars = digit + big + small + symvols + neformal

for _ in range(kolvo):
    for _ in range(len_parol):
        print(random.choice(chars), end='')
    print()