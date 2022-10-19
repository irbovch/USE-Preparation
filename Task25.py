# Найдите все натуральные числа, N, принадлежащие отрезку [100 000 000; 300 000 000], которые можно представить
# в виде N = 2m•7n, где m – чётное число, n – нечётное число. В ответе запишите все найденные числа в порядке
# возрастания, а справа от каждого числа – сумму m+n.

for m in range(0, 1000):
    for n in range(0, 1000):
        if m % 2 == 0 and n % 2 == 1:
            if 100000000 < ((2 ** m) * (7 ** n)) < 300000001:
                print(((2 ** m) * (7 ** n)), "Сумма чисел:", m+n)
                      
# Никита Попов:
for N in range(100000000, 300000001): # пробегаем весь отрезок
    m = 0 # количество 2
    n = 0 # количество 7
    current_N = N # текущее проверяемое
    while current_N % 2 == 0: # пока текущее делится на 2
        current_N //= 2 # делим нацело на 2
        m += 1 # увеличиваем счетчик двоек
    if m % 2 == 0: # если m - четное число (из условия)
        while current_N % 7 == 0: # пока текущее делится на 7
            current_N //= 7 # делим нацело на 7
            n += 1 # увеличиваем счетчик семерок
    if n % 2 != 0 and current_N == 1: # если n - четное число и current_N = 1 (число поделилось на 2 и 7 до конца)
        print(N, m + n) # печатаем
