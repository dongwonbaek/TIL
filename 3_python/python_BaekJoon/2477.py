import sys
from collections import deque
sys.stdin = open('2477.txt')

K = int(input())
matrix = deque()
result = []
answer = []
sampling = []
for _ in range(6):
    D, W = map(int, input().split())
    matrix.append((D, W))
    result.append(D)
for a in range(1, 5):
    if result.count(a) == 1:
        answer.append(a)
for b in range(6):
    if matrix[0][0] != answer[0] and matrix[0][0] != answer[1]:
        sampling.append(matrix.popleft())
    else:
        break
for i in sampling:
    matrix.append(i)
cnt1 = 1
cnt2 = 0
for c in range(6):
    if matrix[c][0] != answer[0] and matrix[c][0] != answer[1]:
        cnt2 = matrix[c + 1][1] * matrix[c + 2][1]
        break
for d in range(6):
    if matrix[d][0] == answer[0] or matrix[d][0] == answer[1]:
        cnt1 *= matrix[d][1]
print((cnt1 - cnt2) * K)