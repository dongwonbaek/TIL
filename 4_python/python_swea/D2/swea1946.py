import sys
sys.stdin = open('swea1946.txt')

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    number_list =[]
    cnt = 1
    for a in range(N):
        x, y = map(int, sys.stdin.readline().split())
        number_list.append([x, y])
    number_list.sort()
    mx = number_list[0][1]
    for b in range(1, N):
        if mx > number_list[b][1]:
            cnt += 1
            mx = number_list[b][1]
    print(cnt)