import sys
sys.stdin = open('1072.txt')

X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z == 100 or Z == 99:
    print(-1)
else:
    cnt = 0
    while True:
        Y += 1
        X += 1
        cnt += 1
        z = (Y * 100) // X
        if Z != z:
            print(cnt)
            break