import sys
sys.stdin = open('1217.txt')
def hamsu(x, y):
    if y == 1:
        return x
    else:
        return x * hamsu(x, y - 1)

for _ in range(1, 11):
    number = int(input())
    i, j = map(int, input().split())
    print(f'#{_} {hamsu(i, j)}')