import sys
sys.stdin = open('1209.txt')

for _ in range(1, 11):
    number = int(input())
    matrix = [list(map(int, input().split())) for i in range(100)]
    biggest = []
    for a in range(100):
        biggest.append(sum(matrix[a]))
    for b in range(100):
        sampling = 0
        for c in range(100):
            sampling += matrix[c][b]
        biggest.append(sampling)   
    dx = [1, -1]
    dy = [1, 1]
    for d in range(2):
        sampling = 0
        if d == 0:
            x = 0
            y = 0
        else:
            x = 99
            y = 0
        for g in range(99):
            sampling += matrix[x][y]
            x += dx[d]
            y += dy[d]
        biggest.append(sampling)
    print(f'#{_} {max(biggest)}')