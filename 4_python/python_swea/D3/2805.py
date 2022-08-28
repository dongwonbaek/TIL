import sys
sys.stdin = open('2805.txt')

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for i in range(N)]
    check = [[False] * N for j in range(N)]
    a = int((N - 1) / 2)
    b = a + 1
    switch = True
    for c in range(N):
        for d in range(a, b):
            check[c][d] = True
        if a == 0:
            switch = False
        if switch == True:
            a -= 1
            b += 1
        else:
            a += 1
            b -= 1
    result = 0
    for x in range(N):
        for y in range(N):
            if check[x][y] == True:
                result += int(matrix[x][y])
    print(f'#{_} {result}')