# 369
import sys
input = sys.stdin.readline

n = int(input())

answer = 0
for i in range(1,n+1):
    s = list(str(i))

    if "3" in s or "6" in s or "9" in s:
        answer += s.count("3")
        answer += s.count("6")
        answer += s.count("9")

print(answer)