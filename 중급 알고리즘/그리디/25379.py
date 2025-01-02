# 피하자

n = int(input())

arr = list(map(int, input().split()))


cnt_even = 0
cnt_even_left = 0
cnt_odd = 0
cnt_odd_left = 0

for i in arr:
    if i % 2 == 0:
        cnt_even += 1
        cnt_odd_left += cnt_odd
    else:
        cnt_odd += 1
        cnt_even_left += cnt_even

print(min(cnt_even_left, cnt_odd_left))