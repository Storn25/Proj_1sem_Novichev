# C начала суток прошло N секунд(N - целое). Найти количество минут, прошедших с начала последнего часа.
N = input('Введите N: ')

while type(N) != int:  # Обработка исключений.
    try:
        N = int(N)
    except ValueError:
        print('Вы ввели не целое число')
        N = input('Введите N: ')

N = N % 3600 // 60
print(f'С начала последнего часа прошло: {N} минут.')
