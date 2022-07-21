import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = map(int,input().split())
    result = 0
    for b in a:
        if b % 2 != 0:
            result += b
    print(f'#{test_case} {result}')
