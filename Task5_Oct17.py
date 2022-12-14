# Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
# 1) Строится двоичная запись числа N.
# 2) К этой записи справа дописывается 0, если число нечетное, и слева 1 в обратном случае.
# 3) Если единиц в двоичном числе получилось четное количество, справа дописывается 1, иначе 0.
# Например, двоичная запись 1010 числа 10 будет преобразована в 110100.
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
# является двоичной записью числа – результата работы данного алгоритма.
# Укажите минимальное число N, для которого результат работы алгоритма будет больше 228.
# В ответе это число запишите в десятичной системе счисления.
Number = 0
for N in range (0, 1000):
    if N % 2 == 1:
        N = bin(N) [2:]
        N = str(N)
        N = N + "0"
    else:
        N = bin(N) [2:]
        N = str (N)
        N = "1" + N
    if N.count ("1") % 2 == 0:
        N = N + "1"
    else:
        N = N + "0"
    N = int (N, 2)
    Number = Number + 1
    if N > 228:
        print (Number, N)
