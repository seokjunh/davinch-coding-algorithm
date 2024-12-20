num = 100_000_0

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

result = 0
for i in range(2, num+1):
    if is_prime(i):
        result += 1
    
print(f'2부터 {num}까지 소수는 총 {result}개 있습니다.')