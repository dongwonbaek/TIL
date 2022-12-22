import sys
sys.stdin = open('1012.txt')

from collections import deque
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    for a in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    for y in range(N):
        for x in range(M):
            if visited[y][x] == 0:
                visited[y][x] = 1
                if matrix[y][x] == 1:
                    list_deque = deque()
                    list_deque.append((x, y))
                    while list_deque:
                        fxfy = list_deque.popleft()
                        for a in range(4):
                            fx = fxfy[0] + dx[a]
                            fy = fxfy[1] + dy[a]
                            if M - 1 >= fx >= 0 and  N - 1 >= fy >= 0:
                                if matrix[fy][fx] == 1 and visited[fy][fx] == 0:
                                    visited[fy][fx] = 1
                                    list_deque.append((fx, fy))
                    cnt += 1
    print(cnt)