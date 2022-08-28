import sys

sys.stdin = open('1873.txt')
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
tank = '><^v'
manual = 'RLUD'
T = int(input())
for _ in range(1, T + 1):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    N = int(input())
    order = input()
    x = 0
    y = 0
    for Y in range(H):
        for X in range(W):
            if matrix[Y][X] in tank:
                y = Y
                x = X
                break
        if x == X:
            break
    for a in order:
        if a in manual:
            location = manual.index(a)
            mx = x + dx[location]
            my = y + dy[location]
            if W > mx >= 0 and H > my >= 0 and matrix[my][mx] == '.':
                matrix[my][mx] = tank[location]
                matrix[y][x] = '.'
                x += dx[location]
                y += dy[location]
            else:
                matrix[y][x] = tank[location]
        else:
            dir = tank.index(matrix[y][x])
            sx = x + dx[dir]
            sy = y + dy[dir]
            while 0 <= sx < W and 0 <= sy < H:
                if matrix[sy][sx] == '*':
                    matrix[sy][sx] = '.'
                    break
                elif matrix[sy][sx] == '#':
                    break
                sx += dx[dir]
                sy += dy[dir]
    
    print(f'#{_}', end = ' ')
    for i in matrix:
        result = ''
        for j in range(W):
            result += i[j]
        print(result)
            

