# 햄버거 분배

n, k = map(int, input().split())
s = input()

eated = [0] * n

answer = 0
for i in range(n):

    if s[i] == "P":
        for j in range(i-k, i+k+1):
            if 0 <= j < n:
                if s[j] == "H" and eated[j] == 0:
                    eated[j] = 1
                    answer += 1
                    break
print(answer)

