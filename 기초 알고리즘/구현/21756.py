# 지우개

n = int(input())

arr = [i for i in range(1,n+1)]

while True:
    if len(arr) == 1:
        print(arr[0])
        break

    for i in range(len(arr)):
        if i % 2 == 0:
            arr.pop(0)
        else:
            arr.append(arr.pop(0))