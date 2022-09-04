import sys
sys.stdin = open('2635.txt')

len_ = 0
N = int(input())
for a in range(1, N + 1):
    result = [N]
    result.append(a)
    while True:
        if result[-2] - result[-1] >= 0:
            result.append(result[-2] - result[-1])
        else:
            break
    if len(result) > len_:
        len_ = len(result)
        result_answer = result
print(len_)
print(*result_answer)