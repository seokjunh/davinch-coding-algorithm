# 터렛

n = int(input())

for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())

    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    diff = abs(r1-r2)

    answer = 0
    
    if diff == 0 and dist == 0:
        answer = -1
    elif dist == r1+r2 or dist == diff:
        answer = 1
    elif diff < dist < r1+r2:
        answer = 2
    
    print(answer)


