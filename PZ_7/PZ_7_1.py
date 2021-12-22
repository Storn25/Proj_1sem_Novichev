# Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S вставить строку S0.

c = input('Введите символ C: ')
s = input('Введите строку S: ')
s0 = input('Введите строку S0: ')
result = ''

for i in s:
    if i == c:
        result += s0
    result += i

print('Результат:', result)
