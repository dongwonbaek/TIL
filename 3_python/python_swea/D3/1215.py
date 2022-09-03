import sys
sys.stdin = open('1215.txt')

for _ in range(1, 11):
    number = int(input())
    matrix = [input() for a in range(8)]
    cnt = 0

    for b in range(9 - number):
        for c in range(8):
            word = ''
            for d in range(number):
                word += matrix[c][b + d]
            if word == word[::-1]:
                cnt += 1
            word = ''
            for d in range(number):
                word += matrix[b + d][c]
            if word == word[::-1]:
                cnt += 1
    print(f'#{_} {cnt}')