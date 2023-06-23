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
        for b in answer:        # 순회는 오름차순 정렬이 되어있기 때문에 
            if a < b:           # 넣으려는 값이 리스트 내 인스턴스보다 작은지만 검사하여 걸러내면 된다.
                switch = False
                break
        if switch == True:
            answer.append(a)
            back()
            answer.pop()

back()