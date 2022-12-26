import sys
sys.stdin = open('1024.txt')

N, L = map(int, input().split())
switch = True
while switch:
    cal = 0
    for a in range(1, L):
        cal += a
    if cal > N:
        print(-1)
        break
    if (N - cal) % L == 0:
        switch = False
        for b in range(L):
            print(((N - cal) // L) + b, end=' ')
    else:
        L += 1
        if L > 100:
            print(-1)
            switch = False