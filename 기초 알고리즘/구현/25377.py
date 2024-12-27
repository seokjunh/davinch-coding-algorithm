# 빵

n = int(input())

answer = 1001
for _ in range(n):
    arrive_time, open_time = map(int, input().split())

    if arrive_time > open_time:
        continue

    if answer > open_time:
        answer = open_time
    
if answer == 1001:
    print(-1)
else:
    print(answer)