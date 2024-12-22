# 1. 큰 수로 작은 수를 나눈다.
# 2. 나머지가 0이면 작은 수가 최대공약수가 된다.
# 3. 나머지가 0이 아니면 작은 수가 큰 수가 되고, 나머지를 작은 수로 대체하고 1번으로 돌아간다.

def gcd(a,b):
    while b:
        a,b = b, a%b
        return a
    
# 최소공배수
def lcm(a,b):
    return (a*b) // gcd(a,b)

print(gcd(510,210))