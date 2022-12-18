import sys
sys.stdin = open('1003.txt')

T = int(input())

for _ in range(T):
    result = [1, 0]
    a = int(input())
    for b in range(a):
        result = [result[1], result[0] + result[1]]
    print(result[0], result[1])