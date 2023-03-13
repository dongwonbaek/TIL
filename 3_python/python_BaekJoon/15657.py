import sys
sys.stdin = open('15657.txt')

N, M = map(int, input().split())
list_ = list(map(int, input().split()))
list_.sort()
answer = []

def back():
    if len(answer) == M:
        print(*answer)
        return
    for a in list_:
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