# 카드 바꾸기

n = int(input())

arr = [0]+list(map(int, input().split()))

answer = 1e9
for i in range(1, n):
    for j in range(i+1, n+1):
        c = (arr[j] - arr[i]) / (j - i)

        if c - int(c) != 0: continue

        s = arr[i] - i * c

        cnt = 0
        for k in range(1,n+1):
            s += c
            if arr[k] != s:
                cnt += 1

        answer = min(answer, cnt)

print(answer)