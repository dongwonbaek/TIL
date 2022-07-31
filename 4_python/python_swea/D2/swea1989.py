import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = input()
    if a[::] == a[::-1]:        # 슬라이싱을 활용하여 입력값을 비교
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')