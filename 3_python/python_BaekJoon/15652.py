import sys
sys.stdin = open('15652.txt')

N, M = map(int, input().split())
answer = []

def back():
    if len(answer) == M:
        print(*answer)
        return
    for a in range(1, N + 1):
        switch = True
        for b in answer:
            if a < b:
                switch = False
                break
        if switch == True:
            answer.append(a)
            back()
            answer.pop()

back()