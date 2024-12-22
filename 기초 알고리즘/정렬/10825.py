# 국영수

n = int(input())

arr = []

for _ in range(n):
    name, *score = input().split()
    arr.append((name, *map(int, score)))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])