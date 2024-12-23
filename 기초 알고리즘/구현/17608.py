# 막대기
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    h = int(input())
    arr.append(h)

reverse_arr = arr[::-1]

max_num = 0
answer = 0

for i in reverse_arr:
    if i > max_num:
        max_num = i
        answer += 1

print(answer)
