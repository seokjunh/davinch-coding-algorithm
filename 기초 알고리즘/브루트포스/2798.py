# 블랙잭

n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()

n = len(arr)
answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            c = arr[i] + arr[j] + arr[k]
            if c <= m:
                answer = max(answer,c)

print(answer)