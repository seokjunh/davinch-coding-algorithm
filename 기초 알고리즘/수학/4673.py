# 셀프 넘버

numbers = [0] * (10001)

for i in range(1,10001):
    c = i
    for j in str(i):
        c += int(j)
    if c <= 10000:
        numbers[c] = 1

for i in range(1,len(numbers)):
    if not numbers[i]:
        print(i)
        

