# 요세푸스 문제 0

n, k = map(int, input().split())

arr = list(range(1,n+1))

answer = []

while arr:

    for i in range(k-1):
        arr.append(arr.pop(0))
    
    answer.append(arr.pop(0))

print("<", end="")
print(*answer, sep=", ", end="")
print(">")