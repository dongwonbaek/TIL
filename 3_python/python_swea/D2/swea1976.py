import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    minute_plus = a[1] + a[3]
    final_minute = minute_plus % 60
    final_hour = a[0] + a[2] + (minute_plus // 60)
    if final_hour > 12:
        final_hour -= 12
    print(f'#{test_case} {final_hour} {final_minute}')