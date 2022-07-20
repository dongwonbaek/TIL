import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = int(input())
    result = 0
    for c in range(1, a + 1):
        if c % 2  == 0:
            result -= c
        else:
            result += c
    print(f'#{test_case} {result}')