import sys
sys.stdin = open('1244.txt')

N = int(input())
switches = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(1, N + 1):
            if i % b == 0:
                switches[i - 1] =  abs(switches[i - 1] - 1)
    else:
        for j in range(1, b):
            if b + j <= N and b - j >= 0:
                if switches[b - j - 1] == switches[b + j - 1]:
                    switches[b - j - 1] = abs(switches[b - j - 1] - 1)
                    switches[b + j - 1] = abs(switches[b + j - 1] - 1)
                else:
                    break
        switches[b - 1] = abs(switches[b - 1] - 1)
cnt = 0
for c in switches:
    print(c, end = ' ')
    cnt += 1
    if cnt % 20 == 0:
        print()