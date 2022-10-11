f = open('24.txt')

n = f.read()
n = n.replace('CA', '1')
n = n.replace('DA', '1')
n = n.replace('FA', '1')
n = n.replace('CO', '1')
n = n.replace('DO', '1')
n = n.replace('FO', '1')

k = 0
kMax = 0

for i in range(0, len(n)):
    if n[i] == '1':
        k = k+1
        kMax = max(k, kMax)
    else:
        k = 0
print(kMax)