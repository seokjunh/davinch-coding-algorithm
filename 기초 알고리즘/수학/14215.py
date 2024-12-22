# 세 막대

arr = list(map(int, input().split()))

arr.sort()

a,b,c = arr[0],arr[1],arr[2]

if a + b <= c:
    c = a + b - 1

print(a+b+c)
