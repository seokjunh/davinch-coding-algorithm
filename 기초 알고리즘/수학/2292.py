# 벌집

n = int(input())

i = 1
answer = 1

while i < n:
    i = i + 6 * answer
    answer += 1
    
print(answer)