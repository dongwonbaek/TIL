import sys
sys.stdin = open('swea2005.txt')

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    number = 1
    a = 0
    result = [[1], [1, 1]]
    while number < N:
        ls_num = [1]
        for b in range(a + 1):
            ls_num.append(result[number][b] + result[number][b + 1])
        ls_num.append(1)
        result.append(ls_num)
        number += 1
        a += 1
    cnt = 0
    print(f'#{_}')
    for c in result:
        print(*c)
        cnt += 1
        if cnt == N:
            break