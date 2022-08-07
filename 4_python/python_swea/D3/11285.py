# 다트게임
N = int(input())
for test_case in range(1, N + 1):
    a = int(input())
    cnt = 0
    c = 20
    for b in range(a):
        x, y = input().split()
        pie = int(x)**2 + int(y)**2
        if pie <= c**2:
            cnt += (11 - (c / 20))
            break
        else:
            c += 20
        if c > 200:
            break
    print(f'#{test_case} {int(cnt)}')