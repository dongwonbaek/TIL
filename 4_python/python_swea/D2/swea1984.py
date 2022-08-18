import sys
from collections import deque
sys.stdin = open('swea1984.txt')

T = int(input())
for _ in range(1, T + 1):
    list_ = deque(sorted(list(map(int, input().split()))))
    list_.pop()
    list_.popleft()
    result = round(sum(list_)/len(list_))
    print(f'#{_} {result}')
