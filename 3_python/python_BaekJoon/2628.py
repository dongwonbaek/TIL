import sys
sys.stdin = open('2628.txt')

N, M = map(int, input().split())
T = int(input())
garo = [0, M]
sero = [0, N]
for _ in range(T):
    a, b = map(int, input().split())
    if a == 1:
        sero.append(b)
    else:
        garo.append(b)
garo.sort()
sero.sort()
garo_largest = 0
sero_largest = 0
for i in range(1, len(garo)):
    if garo[i] - garo[i - 1] > garo_largest:
        garo_largest =  garo[i] - garo[i - 1]
for i in range(1, len(sero)):
    if sero[i] - sero[i - 1] > sero_largest:
        sero_largest =  sero[i] - sero[i - 1]
print(garo_largest * sero_largest)