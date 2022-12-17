import sys
sys.stdin = open('1002.txt')

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    distance2 = (r1 + r2) ** 2
    if distance1 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance1 == distance2:
            print(1)
        elif distance1 < distance2:
            if (r2 - r1) ** 2 == distance1:
                print(1)
            elif(r2 - r1) ** 2 > distance1:
                print(0)
            else:
                print(2)
        else:
            print(0)