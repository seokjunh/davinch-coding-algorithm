# 신기한 수

import sys

input = sys.stdin.readline

n = int(input())

answer = 0

def special_num(n):
    c = n
    d = 0
    for i in str(n):
        d += int(i)
    if c % d == 0:
        return True
    return False

for i in range(1,n+1):
    if special_num(i):
        answer += 1
print(answer)