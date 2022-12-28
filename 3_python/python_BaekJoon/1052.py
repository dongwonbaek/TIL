import sys
sys.stdin = open('1052.txt')

N, K = map(int, input().split())
result = []
cnt = 0
fakeN = N
while True:
    if fakeN < 2 ** cnt:
        result.append(2 ** (cnt - 1))
        fakeN -= (2 ** (cnt - 1))
        if fakeN  == 0:
            break
        else:
            cnt = 0
    else:
        cnt += 1
if K < len(result):
    answer = result[K - 1]
    for a in range(K, len(result)):
        answer -= result[a]
    print(answer)
else:
    print(0)