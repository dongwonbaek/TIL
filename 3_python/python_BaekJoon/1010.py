import sys
sys.stdin = open('1010.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = 1 
    for a in range(M, M - N, -1):
        result *= a
    for b in range(N, 0, -1):
        result /= b
    print(round(result))