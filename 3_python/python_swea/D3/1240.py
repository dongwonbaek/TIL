import sys
sys.stdin = open('1240.txt')
password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for a in range(N)]
    word = ''
    switch = True
    for b in range(N):
        for c in range(M - 1, -1, -1):
            if matrix[b][c] == '1':
                for d in range(c - 55, c + 1):
                    word += matrix[b][d]
                switch = False
                break
        if switch == False:
            break
    sampling = ''
    result = []
    for e in range(len(word)):
        sampling += word[e]
        if len(sampling) == 7:
            result.append(password.index(sampling))
            sampling = ''
    holsu = 0
    jaksu = 0
    for g in range(8):
        if g % 2 == 0:
            holsu += result[g]
        else:
            jaksu += result[g]
    if (holsu * 3 + jaksu) % 10 == 0:
        print(f'#{_} {holsu + jaksu}')
    else:
        print(f'#{_} 0')