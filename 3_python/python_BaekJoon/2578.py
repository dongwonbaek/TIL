import sys
sys.stdin = open('2578.txt')

matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))
checking = [[0] * 5 for a in range(5)]
dealer = []
for _ in range(5):
    for a in list(map(int, input().split())):
        dealer.append(a)
counting = 0
switch = False
for a in dealer:
    switching = False
    counting += 1
    for y in range(5):
        for x in range(5):
            cnt = 0
            if matrix[y][x] == a:
                checking[y][x] = 1
                for i in range(5):
                    if sum(checking[i]) == 5:
                        cnt += 1
                    if checking[0][i] + checking[1][i] + checking[2][i] + checking[3][i] + checking[4][i] == 5:
                        cnt += 1
                if checking[0][0] + checking[1][1] + checking[2][2] + checking[3][3] + checking[4][4] == 5:
                    cnt += 1
                if checking[0][4] + checking[1][3] + checking[2][2] + checking[3][1] + checking[4][0] == 5:
                    cnt += 1
                if cnt >= 3:
                    switch = True
                    break
                switching = True
                break
            if switch == True or switching == True:
                break
        if switch == True or switching == True:
            break
    if switch == True:
        break
print(counting)
