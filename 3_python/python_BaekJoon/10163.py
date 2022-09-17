import sys
sys.stdin = open('10163.txt')

N = int(input())
result = []
x, y = 0, 0
for _ in range(N):
    sampling = list(map(int, input().split()))
    if x < sampling[0] + sampling[2]:
        x = sampling[0] + sampling[2]
    if y < sampling[1] + sampling[3]:
        y = sampling[1] + sampling[3]
    result.append(sampling)

paper = 1
checking = [[0] * x for i in range(y)]
for a in result:
    for b in range(a[1], a[1] + a[3]):
        for c in range(a[0], a[0] + a[2]):
            if checking[b][c] != paper:
                checking[b][c] = paper
    paper += 1

for f in range(1, paper):
    cnt = 0
    for d in checking:
        for e in d:
            if e == f:
                cnt += 1
    print(cnt)
