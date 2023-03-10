import sys
sys.stdin = open('15651.txt')

N, M = map(int, input().split())
answer = []

def back():
    if len(answer) == M:
        print(*answer)
        return
    for a in range(1, N + 1):
        answer.append(a)        # 중복이 허용되고 순서도 상관있으므로 순회하며 넣으면 된다.
        back()
        answer.pop()

back()