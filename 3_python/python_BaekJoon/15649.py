import sys
sys.stdin = open('15649.txt')

N, M = map(int, input().split())
answer = []
def back():
    if len(answer) == M:
        print(*answer)
        return
    for a in range(1, N + 1):
        if a not in answer:
            answer.append(a)
            back()
            answer.pop()
            
back()