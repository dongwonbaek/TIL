import sys
sys.stdin = open('1059.txt')

L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.append(0)
S.sort()
for s in range(len(S) - 1):
    if S[s] < n < S[s + 1]:
        A = S[s]
        B = S[s + 1]
        break
    else:
        A = 0
        B = 0
cnt = 0
for a in range(A + 1, B):
    for b in range(a + 1, B):
        if a <= n <= b:
            cnt += 1
     
print(cnt)