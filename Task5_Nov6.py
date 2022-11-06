# (№ 3905) Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
# 1) Строится двоичная запись числа N.
# 2) Подсчитывается количество нулей и единиц в полученной записи. Если их количество одинаково, в конец записи добавляется её последняя цифра. В противном случае в конец записи добавляется цифра, которая встречается реже.
# 3) Шаг 2 повторяется ещё два раза.
# 4) Результат переводится в десятичную систему счисления.
# При каком наименьшем исходном числе N > 90 в результате работы алгоритма получится чётное число, которое не делится на 4?

N = 0
for N in range(90, 120):
    l = N
    N = str(bin(N))
    if N.count("0") == N.count("1"):
        PoslednyaaCifra = N[len(N)-1]
        PoslednyaaCifra = str(PoslednyaaCifra)
        N = N + PoslednyaaCifra
    if N.count("0") < N.count("1"):
        N = N + "0"
    if N.count("0") > N.count("1"):
        N = N + "1"
    if N.count("0") == N.count("1"):
        PoslednyaaCifra = N[len(N)-1]
        PoslednyaaCifra = str(PoslednyaaCifra)
        N = N + PoslednyaaCifra
    if N.count("0") < N.count("1"):
        N = N + "0"
    if N.count("0") > N.count("1"):
        N = N + "1"
    if N.count("0") == N.count("1"):
        PoslednyaaCifra = N[len(N)-1]
        PoslednyaaCifra = str(PoslednyaaCifra)
        N = N + PoslednyaaCifra
    if N.count("0") < N.count("1"):
        N = N + "0"
    if N.count("0") > N.count("1"):
        N = N + "1"
    N = int(N, 2)
    if N % 2 == 0 and N % 4 != 0:
        print(l)
