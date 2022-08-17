import sys
sys.stdin = open('swea1966.txt')
T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    list_ = list(map(int, input().split()))
    list_.sort()
    print(f'#{_}', end = ' ')
    print(*list_)