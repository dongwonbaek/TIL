import sys
sys.stdin = open('1026.txt')

from heapq import heapify, heappop, heappush
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
heapify(B)
heapqa = []
for a in A:
    heappush(heapqa, (-a, a))
cnt = 0
for b in range(N):
    cnt += (heappop(B) * heappop(heapqa)[1])
print(cnt)