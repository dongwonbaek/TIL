import sys
sys.stdin = open('swea1974.txt')

T = int(input())
number_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
for _ in range(1, T + 1):
    sudoku = [list(map(int, input().split()))for a in range(9)]
    for y in range(9):
        garo = []
        sero = []
        switch1 = True
        for x in range(9):
            if sudoku[y][x] in garo:
                switch1 = False
                break
            else:
                garo.append(sudoku[y][x])
            if sudoku[x][y] in sero:
                switch1 = False
                break
            else:
                sero.append(sudoku[x][y])
        if switch1 == False:
            break
    for i in number_list:
        for j in number_list:
            nemo = []
            switch2 = True
            for b in i:
                for c in j:
                    if sudoku[b][c] in nemo:
                        switch2 = False
                        break
                    else:
                        nemo.append(sudoku[b][c])
                if switch2 == False:
                    break
            if switch2 == False:
                break
        if switch2 == False:
            break
    if switch1  == False or switch2 == False:
        print(f'#{_} 0')
    else:
        print(f'#{_} 1')
