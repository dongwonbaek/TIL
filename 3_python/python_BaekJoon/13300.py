import sys
sys.stdin = open('13300.txt')

N, K = map(int, input().split())
sampling = []
for _ in range(N):
    sampling.append(input())
result = list(set(sampling))
counting = []
for a in result:
    counting.append(sampling.count(a))
cnt = 0
for b in counting:
    if b % K > 0:
        cnt += ((b // K) + 1)
    else:
        cnt += (b // K)
print(cnt)