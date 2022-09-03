import sys
sys.stdin = open('1221.txt')

num_example = [
    'ZRO',
    'ONE',
    'TWO',
    'THR',
    'FOR',
    'FIV',
    'SIX',
    'SVN', 
    'EGT',
    'NIN'
]
T = int(input())
for _ in range(1, T + 1):
    number = input().split()
    number_list = input().split()
    sampling = []
    result = []
    for a in number_list:
        sampling.append(num_example.index(a))
    sampling.sort()
    for a in sampling:
        result.append(num_example[a])
    print(f'#{_}')
    print(*result)