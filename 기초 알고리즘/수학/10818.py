# 최소, 최대

n = int(input())

arr = list(map(int, input().split()))

# 1. 내장 함수
print(min(arr),max(arr))

# 2. 반복문
min_num, max_num = arr[0], arr[0]

for a in arr[1:]:
    if a > max_num:
        max_num = a
    elif a < min_num:
        min_num = a

print(min_num, max_num)
