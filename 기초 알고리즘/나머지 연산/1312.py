# 소수수

a,b,n = map(int, input().split())

ans = 0

for _ in range(n):
    a = a % b
    a *= 10
    ans = a // b

print(ans)