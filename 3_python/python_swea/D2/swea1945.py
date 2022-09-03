T = int(input())
num_list = [2, 3, 5, 7, 11]
for _ in range(1, T + 1):
    x = int(input())
    result = []
    for a in num_list:
        cnt = 0
        while x % a == 0:
            if x % a == 0:
                x //= a
                cnt += 1
        result.append(cnt)
    print(f'#{_}', end = ' ')
    for b in result:
        print(b, end = ' ')
    print()