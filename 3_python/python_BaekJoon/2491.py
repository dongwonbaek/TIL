import sys
sys.stdin = open('2491.txt')

N = int(input())
a = list(map(int, input().split()))
length = 1
length_max = 1
length_max1 = 1
for i in range(0, N - 1):
    if a[i + 1] - a[i] >= 0:
        length += 1
    else:
        length = 1
    if length_max <= length:
        length_max = length
length = 1
for i in range(0, N - 1):
    if a[i + 1] - a[i] <= 0:
        length += 1
    else:
        length = 1
    if length_max1 <= length:
        length_max1 = length

print(max(length_max, length_max1))