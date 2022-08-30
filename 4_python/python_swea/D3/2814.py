import sys
sys.stdin = open('2814.txt')

T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    path = [[] for i in range(N + 1)]
    result = []
    for a in range(M):
        x, y = map(int, input().split())
        if y not in path[x]:
            path[x].append(y)
        if x not in path[y]:
            path[y].append(x)
    for b in range(1, N + 1):
        stack = [b]
        distance_ = [0] * (N + 1)
        distance_[b] = 1
        while len(stack) != 0:
            fx = stack.pop()
            
            for c in path[fx]:
                if distance_[c] == 0:
                    stack.append(c)
                    distance_[c] += (distance_[fx] + 1)
        result.append(max(distance_))
    fianl_result = max(result)
    print(f'#{_} {max(result)}')
