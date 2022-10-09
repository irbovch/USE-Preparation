print("Введите число:")
s = l = int(input())
n = 740
while s+n<1200:
  s = s + 6
  n = n - 4
if n == 68:
    print ("Нашли число:", l, "При нем n равен 68")