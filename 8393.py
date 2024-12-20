# 합

n = int(input())
#1. for 문

s1 = 0
for i in range(1,n+1):
    s1 += i
print(s1)

#2. while 문
s2 = 0
i = 1
while i <= n:
    s2 += i
    i += 1
print(s2)

#3. 내장 함수
s3 = sum(range(1,n+1))
print(s3)

#4. 수열의 합 공식
s4 = (n+1) * n // 2
print(s4)