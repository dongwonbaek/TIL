import sys
sys.stdin = open('swea1954.txt')

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for h in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    number = 1
    x = 0
    y = 0
    a = 0
    matrix[x][y] = 1
    while number <= N ** 2 - 1:
        if 0 <= x + dx[a % 4] < N and 0 <= y + dy[a % 4] < N:
            if matrix[x + dx[a % 4]][y + dy[a % 4]] == 0:
                x += dx[a % 4]
                y += dy[a % 4]
                number += 1
                matrix[x][y] = number
            else:
                a += 1
        else:
            a += 1
    print(f'#{_}')
    for a in matrix:
        print(*a)