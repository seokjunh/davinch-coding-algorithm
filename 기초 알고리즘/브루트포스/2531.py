# 회전초밥
import sys

input = sys.stdin.readline

n,d,k,c = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

cnt = 1
check = [0] * (d+1)
check[c] = 1
for i in range(k):
    idx = arr[i]
    check[idx] += 1
    if check[idx] == 1:
        cnt += 1

answer = cnt

for i in range(n-1):
    check[arr[i]] -= 1
    if check[arr[i]] == 0:
        cnt -= 1
    
    check[arr[(i+k)%n]] += 1
    if check[arr[(i+k)%n]] == 1:
        cnt += 1
    
    answer = max(answer, cnt)

print(answer)
