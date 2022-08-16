import sys
sys.stdin = open('swea1961.txt')
T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    result1 = [[0] * N for h in range(N)]
    result2 = [[0] * N for h in range(N)]
    result3 = [[0] * N for h in range(N)]
    matrix = [list(map(int, input().split())) for a in range(N)]
    for y in range(N):
        for x in range(N):
            result1[y][N - x - 1] = matrix[x][y]
            result2[N - x - 1][N - y - 1] = matrix[x][y]
            result3[N - y - 1][x] = matrix[x][y]
    print(f'#{_}')
    for b in range(N):
        for c in range(N):
            print(result1[b][c], end = '')
        print('', end = ' ')
        for c in range(N):
            print(result2[b][c], end = '')
        print('', end = ' ')
        for c in range(N):
            print(result3[b][c], end = '')
        print()
