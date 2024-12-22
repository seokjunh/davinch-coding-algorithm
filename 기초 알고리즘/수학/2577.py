# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

s = a*b*c

for i in range(10):
    print(str(s).count(str(i)))