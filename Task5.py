# Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
# 1) Строится двоичная запись числа N.
# 2) Складываются все цифры полученной двоичной записи. В конец записи (справа) дописывается остаток от деления полученной суммы на 2.
# 3) Если количество единиц в двоичной записи числа N больше количества нулей, справа дописывается 0, иначе 1.
# 4) Результат переводится в десятичную систему счисления.
# Сколько различных чисел, принадлежащих отрезку [50; 80], может получиться в результате работы автомата?

AllEndNumbers = []
for n in range(0, 10000):
    s = bin(n)[2:]
    s = str(s)
    Pripiska = s.count("1") % 2
    if Pripiska == 1:
        s += "1"
    else:
        s += "0"
    if s.count("1") > s.count("0"):
        s = s + "0"
    else:
        s = s + "1"
    r = int(s , 2)
    if r in range(50, 81):
        print("Из числа", n, "получилось", r)
        AllEndNumbers.append(r)
UniqueNumbers = set(AllEndNumbers)
ListOfUnique = list(UniqueNumbers)
AmountOfUnique = len(ListOfUnique)
print("Всего уникальных чисел:", AmountOfUnique)