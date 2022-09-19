import sys
sys.stdin = open('2563.txt')

N = int(input())
checking = [[0] * 100 for i in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            checking[i][j] = 1
cnt = 0
for a in checking:
    for b in a:
        if b == 1:
            cnt += 1
print(cnt)