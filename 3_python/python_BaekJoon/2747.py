import sys
sys.stdin = open('2747.txt')

n = int(input())
result = [0] * (n + 1)
result[1] = 1
if n >= 2:
    for a in range(2, n + 1):
        result[a] = result[a - 1] + result[a - 2]
print(result[n])