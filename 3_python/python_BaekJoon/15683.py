import sys
sys.stdin = open('15683.txt')

matrix = []
N, M = map(int, input().split())
for _ in range(N):
    matrix.append(list(map(int, input().split())))
cctv = []
first = [(1, 0), (0, 1), (-1, 0), (0, -1)]
second = [(1, 0), (0, 1)]
third = []
for y in range(N):
    for x in range(M):
        if 1 <= matrix[y][x] <= 5 :
            cctv.append(matrix[y][x])
