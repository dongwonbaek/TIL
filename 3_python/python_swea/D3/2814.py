import sys
sys.stdin = open('2814.txt')

def dfs(idx, cnt):
    global max
    visit[idx] = True
    if cnt > max:
        max = cnt
    for c in matrix[idx]:
        if visit[c] == False:
            dfs(c, cnt + 1)
            visit[c] = False

T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[] for i in range(N + 1)]
    for a in range(M):
        x, y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)
    max = 0

    for b in range(1, N + 1):
        visit = [False] * (N + 1)
        dfs(b, 1)
    print(f'#{_} {max}')



# def dfs(idx,cnt):
#     global max
#     visit[idx] = True
#     if cnt > max:
#         max = cnt
#     for i in s[idx]:
#         if not visit[i]:
#             dfs(i,cnt+1)
#             visit[i] = 0

# T = int(input())
# for _ in range(1, T + 1):
#     n,m = map(int,input().split())
#     s=[[] for i in range(n+1)]
#     for i in range(m):
#         x,y = map(int,input().split())
#         s[x].append(y)
#         s[y].append(x)
#     max = 0

#     for i in range(1,n+1):
#         visit = [0] * (n+1)
#         dfs(i,1)
#     print(f'#{_} {max}')


# T = int(input())
# for _ in range(1, T + 1):
#     N, M = map(int, input().split())
#     path = [[] for i in range(N + 1)]
#     result = []
#     for a in range(M):
#         x, y = map(int, input().split())
#         if y not in path[x]:
#             path[x].append(y)
#         if x not in path[y]:
#             path[y].append(x)
#     for b in range(1, N + 1):
#         stack = [b]
#         distance_ = [0] * (N + 1)
#         distance_[b] = 1
#         while len(stack) != 0:
#             fx = stack.pop()
#             distance_[fx] = 
#             for c in path[fx]:
#                 if distance_[c] == 0:
#                     stack.append(c)
#                     distance_[c] += (distance_[fx] + 1)
#         result.append(max(distance_))
#     fianl_result = max(result)
#     print(f'#{_} {max(result)}')

