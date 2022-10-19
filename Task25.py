for N in range (100000000, 300000001):
    if N % 2 == 0:
        for m in range (0, 1000):
            for n in range (0, 1000):
                if m % 2 == 0 and n % 2 == 1:
                    if ((2 ** m) * (7 ** n)) > 100000000 and ((2 ** m) * (7 ** n)) < 300000001:
                        print (((2 ** m) * (7 ** n)), "Сумма чисел:", m+n)