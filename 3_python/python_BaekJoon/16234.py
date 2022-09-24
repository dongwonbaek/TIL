import sys
sys.stdin = open('16234.txt')
from copy import deepcopy
import math

N, L, R = map(int, input().split())
matrix = []
checking = [[0] * N for _ in range(N)]
dx = [1, 0]
dy = [0, 1]
empire = 1
answer = 0
for _ in range(N):
    matrix.append(list(map(int, input().split())))
previous = deepcopy(matrix)
while True:
    for y in range(N):
        for x in range(N):
            for a in range(2):
                mx = x + dx[a]
                my = y + dy[a]
                if mx <= N - 1 and my <= N - 1:
                    if R >= abs(matrix[y][x] - matrix[my][mx]) >= L:
                        if checking[y][x] == 0:
                            checking[y][x] = empire
                            checking[my][mx] = empire
                            empire += 1
                        else:
                            checking[my][mx] = checking[y][x]
    for b in range(1, empire + 1):
        cnt = 0
        result = 0
        for y in range(N):
            for x in range(N):
                if checking[y][x] == b:
                    cnt += 1
                    result += matrix[y][x]
        if cnt > 0:
            aftermove = math.trunc(result / cnt)
        for y in range(N):
            for x in range(N):
                if checking[y][x] == b:
                    matrix[y][x] = aftermove
    if previous != matrix:
        previous = deepcopy(matrix)
        answer += 1
    else:
        print(answer)
        break