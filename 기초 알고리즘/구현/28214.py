# 크림빵

n,k,p = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
for i in range(0,n*k,k):
    
    cnt = list(map(str,arr[i:i+k])).count("0")

    if cnt < p:
        answer += 1

print(answer)
