import sys
sys.stdin = open('swea1948.txt')

years = [(0, 0), (1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
T = int(input())
for _ in range(1, T + 1):
    result = 0
    days = list(map(int, input().split()))
    for a in range(days[0], days[2]):
        result += years[a][1]
    result += (days[3] - days[1] + 1)
    print(f'#{_} {result}')