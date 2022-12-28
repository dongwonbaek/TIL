import sys
sys.stdin = open('1051.txt')

N, M = map(int, input().split())
matrix = []
min_square = min(N, M)
for _ in range(N):
    matrix.append(input())
switch = True
for a in range(min_square, 0, -1):
    if a == 1:
        print(1)
        break
    for b in range(N - a + 1):
        for c in range(M - a + 1):
            if matrix[b][c] == matrix[b][c + a - 1] and matrix[b][c] == matrix[b + a - 1][c] and matrix[b][c] == matrix[b + a - 1][c + a - 1]:
                print(a ** 2)
                switch = False
            if switch == False:
                break
        if switch == False:
            break
    if switch == False:
        break
