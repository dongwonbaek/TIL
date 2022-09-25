import sys
sys.stdin = open('1769.txt')

X = input()
def third(i, cnt):
    result = 0
    if len(i) > 1:
        cnt += 1
        for a in i:
            result += int(a)
        third(str(result), cnt)
    elif len(i) == 1:
        print(cnt)
        if i in ['3', '6', '9']:
            print('YES')
        else:
            print('NO')

third(X, 0)