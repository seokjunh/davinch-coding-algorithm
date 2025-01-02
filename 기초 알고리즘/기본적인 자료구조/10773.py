# 제로

n = int(input())

answer = []

for _ in range(n):
    x = int(input())

    if x == 0:
        answer.pop()
    else:
        answer.append(x)

print(sum(answer))