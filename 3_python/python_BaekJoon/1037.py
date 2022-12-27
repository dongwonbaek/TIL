import sys
sys.stdin = open('1037.txt')

N = int(input())
num_list = list(map(int, input().split()))
result = max(num_list) * min(num_list)
print(result)