import sys
sys.stdin = open('17406.txt')

N, M, K = map(int, input().split())
matrix = []
order = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
for _ in range(K):
    order.append(list(map(int, input().split())))

min_x = order[0][1] - order[0][2]
max_x = order[0][1] + order[0][2]
min_y = order[0][0] - order[0][2]
max_y = order[0][0] + order[0][2]