import sys
sys.stdin = open('1213.txt', encoding = 'UTF8')

for _ in range(1, 11):
    number = input()
    word = input()
    result = ''
    cnt = 0
    for a in input():
        result += a
        if word in result:
            cnt += 1
            result = ''
    print(f'#{_} {cnt}')