# 박 터뜨리기

n, k = map(int, input().split())

basket = [0] * k

for i in range(1,k+1):
    basket[i-1] = i
    n -= i

if n < 0:
    print(-1)
else:
    while n > 0:
        
        for i in range(k-1,-1,-1):
            basket[i] += 1
            n -= 1
            if n == 0:
                break
    print(basket[-1] - basket[0])    