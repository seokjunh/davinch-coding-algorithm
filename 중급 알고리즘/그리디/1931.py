# 회의실 배정

n = int(input())

arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s,e))

sorted_arr = sorted(arr, key=lambda x: (x[1],x[0]))

stack = []
for i in sorted_arr:
    if not stack:
        stack.append(i)
    else:
        if stack[-1][1] <= i[0]:
            stack.append(i)

print(len(stack))



