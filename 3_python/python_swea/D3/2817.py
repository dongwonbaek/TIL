from itertools import combinations
import sys

sys.stdin = open("2817.txt")
T = int(input())
for _ in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for a in range(1, N + 1):
        result = combinations(A, a)
        for b in result:
            if sum(b) == K:
                cnt += 1
    print(f"#{_} {cnt}")
