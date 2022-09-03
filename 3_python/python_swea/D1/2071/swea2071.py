import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    print(f'#{test_case}', round(sum(a)/len(a)), sep = ' ')