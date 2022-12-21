import sys
sys.stdin = open('1009.txt')

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    realb = b % 4
    if realb == 0:
        realb = 4
    result = (a ** realb) % 10
    if result == 0:
        result = 10
    print(result)