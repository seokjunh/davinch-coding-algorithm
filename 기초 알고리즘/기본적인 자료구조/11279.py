# 최대 힙

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(heap,-x)
    else:
        if not heap:
            print(0)
        else:
            v = heapq.heappop(heap)
            print(-v)
