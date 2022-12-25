import sys
sys.stdin = open('1021.txt')

from collections import deque
N, M = map(int, input().split())
index_list = list(map(int, input().split()))  
cnt = 0
num_list = deque(range(1, N + 1))
for a in index_list:
    index_num = num_list.index(a)
    if len(num_list) / 2 > index_num:
        cnt += index_num
        for b in range(index_num):
            num_list.append(num_list.popleft())
        num_list.popleft()
    else:
        indexing = int(round(len(num_list) - index_num))
        cnt += indexing
        for c in range(indexing):
            num_list.appendleft(num_list.pop())
        num_list.popleft()
print(cnt)