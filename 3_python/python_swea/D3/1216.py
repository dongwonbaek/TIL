import sys
sys.stdin = open('1216.txt')

for _ in range(1, 11):
    number = int(input())
    matrix = [input() for __ in range(100)]
    switch = True
    for a in range(100, 0, -1):
        word1 = ''
        word2 = ''
        for d in range(101 - a):
            for b in range(100):
                for c in range(a):
                    word1 += matrix[b][c + d]
                    word2 += matrix[c + d][b]
                if word1 == word1[::-1] or word2 == word2[::-1]:
                    print(f'#{_} {len(word1)}')
                    switch = False
                    break
                else:
                    word1 = ''
                    word2 = ''
            if switch == False:
                break
        if switch == False:
            break
