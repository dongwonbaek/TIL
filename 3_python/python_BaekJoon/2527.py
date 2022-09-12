import sys
sys.stdin = open('2527.txt')

for _ in range(4):
    garo = []
    sero = []
    x, y, p, q, a, b, c, d = map(int, input().split())
    for i in range(x, p + 1):
        if a <= i <= c:
            garo.append(i)
    for j in range(y, q + 1):
        if b <= j <= d:
            sero.append(j)
    garo = len(garo)
    sero = len(sero)
    if garo > 1 and sero > 1:
        print('a')
    elif (garo > 1 and sero == 1) or (garo == 1 and sero > 1):
        print('b')
    elif garo == 1 and sero == 1:
        print('c')
    elif garo == 0 or sero == 0:
        print('d')