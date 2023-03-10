import sys
sys.stdin = open('15650.txt')

N, M = map(int, input().split())
answer = []
def back():
    if len(answer) == M:
        print(*answer)
        return
    for a in range(1, N + 1):
        switch = True
        for b in answer:        # 순회를 통해서 자연스럽게 오름차순으로 정리가 됨
            if a <= b:          # answer에 넣으려는 수가 answer의 인스턴스들보다 큰지만 확인하면 됨.
                switch = False
                break
        if switch == True:
            answer.append(a)
            back()
            answer.pop()
back()