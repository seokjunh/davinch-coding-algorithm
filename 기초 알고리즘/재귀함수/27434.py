# 팩토리얼 3

import sys
sys.setrecursionlimit(10**6)

n = int(input())

def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1)
    
print(facto(n))