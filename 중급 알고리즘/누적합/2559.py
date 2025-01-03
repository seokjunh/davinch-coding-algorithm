# 수열

# 누적합은 범위가 정해지지 않았을 때, 누적합의 배열을 여러번 탐색할 때 효과적
# 범위가 정해져 있고 최대값을 구하는 것이기 때문에 슬라이딩 윈도우 효과적

n,k = map(int, input().split())

arr = list(map(int, input().split()))

result = sum(arr[:k])

temp = result
for i in range(k,n):
    temp += arr[i] - arr[i-k]
    result = max(result, temp)

print(result)