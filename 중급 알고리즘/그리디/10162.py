# 전자레인지

t = int(input())

answer = [0,0,0]
arr = [300, 60, 10]

for i in range(len(arr)):
    answer[i] += t // arr[i]
    t = t % arr[i]

if t != 0:
    print(-1)
else:
    print(*answer)


