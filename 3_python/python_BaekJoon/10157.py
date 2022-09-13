import sys
sys.stdin = open('10157.txt')

C, R = map(int, input().split())
K = int(input())
check = [[0] * C for i in range(R)]
check[0][0] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 1
d_cnt = 0
x = 0
y = 0
answer = 0
while cnt <= C * R:
    if x + dx[d_cnt % 4] <= C - 1 and y + dy[d_cnt % 4] <= R - 1:
        if check[y + dy[d_cnt % 4]][x + dx[d_cnt % 4]] == 0:
            check[y + dy[d_cnt % 4]][x + dx[d_cnt % 4]] = 1
            cnt += 1
            x += dx[d_cnt % 4]
            y += dy[d_cnt % 4]
        else:
            d_cnt += 1
        if cnt == K:
            answer = 1
            break
        if cnt == C * R:
            break
    else:
        d_cnt += 1

if K != 1:
    if answer == 1:
            print(x + 1, y + 1, sep=' ')
    else:
        print(0)
else:
    print(1, 1, sep=' ')