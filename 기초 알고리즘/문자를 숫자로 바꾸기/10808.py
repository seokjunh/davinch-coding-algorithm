# 알파벳 개수

s = input()

answer = [0] * 26

for i in s:
    cnt = s.count(i)
    d = ord(i) - ord("a")
    answer[d] = cnt

print(*answer)