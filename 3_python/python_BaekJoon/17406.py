import sys
sys.stdin = open('17406.txt')

from itertools import permutations
import copy

N, M, K = map(int, input().split())
matrix = []
order = []
result = []
answer = []
final_answer = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    matrix.append(list(map(int, input().split())))
for _ in range(K):
    order.append(list(map(int, input().split())))

for order_part in permutations(order, K):
    result = copy.deepcopy(matrix)
    matrixcopy = copy.deepcopy(matrix)
    for a in order_part:
        checking = [[0] * M for _ in range(N)]
        for b in range(1, a[2] + 1):
            max_x = a[1] - 1 + b
            max_y = a[0] - 1 + b
            min_x = a[1] - 1 - b
            min_y = a[0] - 1 - b 
            x = a[1] - 1 - b
            y = a[0] - 1 - b
            index_cnt = 0
            while True:
                mx = x + dx[index_cnt % 4]
                my = y + dy[index_cnt % 4]
                if max_x >= mx >= min_x and max_y >= my >= min_y and checking[my][mx] == 0:
                    checking[my][mx] = 1
                    result[my][mx] = matrixcopy[y][x]
                    x += dx[index_cnt % 4]
                    y += dy[index_cnt % 4]
                elif mx > max_x or min_x > mx or max_y < my or my < min_y:
                    index_cnt += 1
                elif checking[my][mx] != 0:
                    break
        matrixcopy = copy.deepcopy(result)
    for i in result:
        answer.append(sum(i))
    final_answer.append(min(answer))
print(min(final_answer))