import sys
sys.stdin = open('14696.txt')

N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Alist = [0] * 4
    Blist = [0] * 4
    for a in range(1, 1 + A[0]):
        if A[a] == 4:
            Alist[0] += 1
        elif A[a] == 3:
            Alist[1] += 1
        elif A[a] == 2:
            Alist[2] += 1
        elif A[a] == 1:
            Alist[3] += 1
    for b in range(1, 1 + B[0]):
        if B[b] == 4:
            Blist[0] += 1
        elif B[b] == 3:
            Blist[1] += 1
        elif B[b] == 2:
            Blist[2] += 1
        elif B[b] == 1:
            Blist[3] += 1
    switch = 0
    for i in range(4):
        if Alist[i] > Blist[i]:
            print('A')
            switch = 1
            break
        elif Blist[i] > Alist[i]:
            print('B')
            switch = 1
            break
    if switch == 0:
        print('D')



    # cntA = 0
    # cntB = 0
    # for a in range(1, 1 + A[0]):
    #     cntA += 10**A[a]
    # for b in range(1, 1 + B[0]):
    #     cntB += 10**B[b]
    # if cntA > cntB:
    #     print('A')
    # elif cntA < cntB:
    #     print('B')
    # else:
    #     print('D')