# 대피소

from itertools import combinations

n,k = map(int,input().split())

x = [0]*n
y = [0]*n

for i in range(n):
    a,b = map(int,input().split())
    x[i],y[i] = a,b

comb = list(combinations(range(n),k))

answer = 1e9

for c in comb:
    rst = 0
    for i in range(n):
        min_dist = 1e9
        for j in c:
            dist = abs(x[i]-x[j]) + abs(y[i]-y[j])
            min_dist = min(min_dist, dist)
        rst = max(rst,min_dist)
    answer = min(answer,rst)

print(answer)


