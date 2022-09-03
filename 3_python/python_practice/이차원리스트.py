from pprint import pprint
# N, M = map(int, input().split())
# # matrix = []
# # for _ in range(N):
# #     line = list(map(int, input().split()))
# #     matrix.append(line)

# matrix = [list(map(int, input().split())) for _ in range(N)]
# pprint(matrix)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
pprint(matrix)