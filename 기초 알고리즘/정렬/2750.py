# 수 정렬하기

n = int(input())

# arr = []
# for _ in range(n):
#     arr.append(int(input()))

# arr.sort()

# for i in arr:
#     print(i)

# 버블 정렬 사용

arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

for i in arr:
    print(i)
    