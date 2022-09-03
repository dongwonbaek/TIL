import sys
sys.stdin = open('1206.txt')

dx = [0, 0, 0, 0]
dy = [1, -1, 2, -2]

for _ in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    matrix = [[0] * N for i in range(255)]
    for a in range(N):
        for b in range(254, 254 - height[a], -1):
            matrix[b][a] = 1
    cnt = 0

    for x in range(255):
        for y in range(N):
            switch = True
            if matrix[x][y] == 1:
                for c in range(4):
                    mx = x + dx[c]
                    my = y + dy[c]
                    if matrix[mx][my] == 1:
                        switch = False
                        break
                if switch == True:
                    cnt += 1
    print(f'#{_} {cnt}')