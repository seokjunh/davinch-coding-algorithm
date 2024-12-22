# 회전초밥

n,d,k,c = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

answer = 0
for i in range(len(arr)):
    eat_sushi = 1
    check = [0] * (d+1)
    check[c] = 1
    for j in range(i,i+k):
        idx = arr[j%len(arr)]

        if not check[idx]:
            eat_sushi += 1

        check[idx] = 1
    print(check)
    answer = max(answer, eat_sushi)

print(answer)