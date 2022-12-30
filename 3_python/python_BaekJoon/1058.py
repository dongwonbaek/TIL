import sys
sys.stdin = open('1058.txt')

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(input())

result_cnt = 0
for a in range(N):
    cnt = 0
    result = []
    for b in range(N):
        if matrix[a][b] == 'Y':
            result.append(b)
            for c in range(N):
                if matrix[b][c] == 'Y':
                    result.append(c)
    answer = len(set(result)) - 1
    if answer > result_cnt:
        result_cnt = answer
if result_cnt == -1:
    print(0)
else:
    print(result_cnt)