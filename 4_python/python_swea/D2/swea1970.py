import sys
sys.stdin = open('swea1970.txt')

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for _ in range(1, T + 1):
    money = int(input())
    result = []
    for a in money_list:
        result.append(money // a)
        money %= a
    print(f'#{_}')
    print(*result)