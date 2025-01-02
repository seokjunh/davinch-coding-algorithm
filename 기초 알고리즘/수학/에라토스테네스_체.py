# 어떤 수가 소수인지 알고 싶을 때는 제곱근 방법을 사용하고
# 주어진 범위 내에서 소수를 찾을 때는 에라토스테네스의 체를 사용함.

num = 100_000_0
prime = [True] * (num+1)

prime[0],prime[1] = False, False

for i in range(2, num+1):
    if prime[i]:
        for j in range(i*2, num+1, i):
            prime[j] = False

result = 0
for i in range(num+1):
    if prime[i]:
        result += 1

print(f'2부터 {num}까지 소수는 총 {result}개 있습니다.')
