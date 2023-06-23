import sys
sys.stdin = open('15663.txt')

N, M = map(int, input().split())
list_ = list(map(int, input().split()))
list_.sort()
visited = [False * N]
ans = []


def back():
    if len(ans) == M:
        print(ans)
        return
    for a in range(N):
        ans.append(a)
        back()
        ans.pop()

back()
print(answer)
# result = set(answer)
# for a in result:
#     print(*a)