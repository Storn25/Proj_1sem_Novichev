# Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному числу K слева цифру D
# (D - входной параметр целого типа, лежащий в диапазоне 1-9, K - параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции последовательно добавить к числу K слева данные
# цифры D1 и D2, выводя результат каждого добавления

def addleftdigit(d, k):
    d, k = str(d), str(k)
    k = d + k
    return k


n = int(input('Введите число n: '))
d1 = int(input('Введите число d1: '))
n = addleftdigit(d1, n)
print(n)
d2 = int(input('Введите число d2: '))
n = addleftdigit(d2, n)
print(n)
