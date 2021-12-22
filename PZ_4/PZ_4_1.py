# Дано целое число N(>0). Найти сумму N^2 + (N + 1)^2 + ... + (2N)^2

n = input('Введите целое число(>0): ')
while type(n) != int:
    # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Вы ввели не число')
        n = input('Введите целое число(>0): ')

i = n
summa = 0
while i <= 2*n:
    summa += i ** 2
    i += 1
print('Сумма:', summa)
