import sys
sys.stdin = open('15656.txt')
# 중복을 허용하고, 순서 또한 허용하는 수열을 구하는 문제

N, M = map(int, input().split())
list_ = list(map(int, input().split()))
list_.sort()
answer = []

def back():
    if len(answer) == M:
        print(*answer)
        return
    for a in list_:
        answer.append(a)
        back()
        answer.pop()

back()