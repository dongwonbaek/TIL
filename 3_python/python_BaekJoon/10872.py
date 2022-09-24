import sys
sys.stdin = open('10872.txt')

N = int(input())
result = 1
while N > 0 :
    result *= N
    N -= 1
print(result)