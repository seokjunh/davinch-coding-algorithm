# 곱셈

a,b,c = map(int, input().split())

def recur(a,b):
    if b == 1:
        return a % c

    result = recur(a, b//2)
    
    if b % 2 == 0:
        return (result*result) % c
    else:
        return (result*result*a) % c

print(recur(a,b))