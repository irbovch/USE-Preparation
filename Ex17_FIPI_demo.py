f=open('17.txt')

Pairs=0
MaxSumOfSquares=0

n1 = int(f.readline())

for s in f.readlines():
    n2 = int(s)
    if ((abs(n1) % 10 == 3) != (abs(n2) % 10 == 3)) and (n1**2 + n2**2 >= 9973**2):
        Pairs = Pairs+1
        MaxSumOfSquares = max(MaxSumOfSquares, n1**2 + n2**2)
    n1 = n2
print(Pairs, MaxSumOfSquares)