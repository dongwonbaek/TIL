import sys
sys.stdin = open('9663.txt')

N = int(input())
answer = []
ans = 0

def back():
    global ans
    if len(answer) == N:
        ans += 1
        return
    for a in range(N):
        if len(answer) > 0:
            if a not in answer and abs(a - answer[(len(answer) - 1)]) > 1:
                answer.append(a)
                back()
                answer.pop()
        else:
            answer.append(a)
            back()
            answer.pop()

back()
print(len(ans))