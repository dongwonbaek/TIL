import sys
sys.stdin = open('1860.txt')

T = int(input())
for _ in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive = sorted(list(map(int, input().split())))
    cnt = 0
    idx = 0
    result = []
    switch = True
    for a in range(max(arrive) + 1):
        if (a // M) > 0 and (a % M) == 0:
            cnt += K
            result.append(cnt)
        else:
            result.append(cnt)
    for b in arrive:
        for d in range(b, max(arrive) + 1):
            result[d] -= 1
    for c in result:
        if c < 0:
            switch = False
            break
    if switch == True:    
        print(f'#{_} Possible')
    else:
        print(f'#{_} Impossible')