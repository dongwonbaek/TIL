import sys
sys.stdin = open('1018.txt')

chess = []
N, M = map(int, input().split())
n = N - 7
m = M - 7
for _ in range(N):
    chess.append(input())
result = []
for x in range(n):
    for y in range(m):
        cnt1 = 0
        cnt2 = 0
        for a in range(x, x + 8):
            for b in range(y, y + 8):
                if (a + b) % 2 == 0:
                    if chess[a][b] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if chess[a][b] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        result.append(min(cnt1, cnt2))
print(min(result))