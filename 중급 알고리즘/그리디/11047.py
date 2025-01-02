# 동전 0

n,k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.reverse()

answer = 0
for i in arr:
    if k // i >= 1:
        answer += k // i
        k = k % i

print(answer)