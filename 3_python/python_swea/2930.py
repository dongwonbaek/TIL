import sys

sys.stdin = open("2930.txt")
import heapq


for _ in range(1, int(input()) + 1):
    list_ = []
    result = []
    for a in range(int(input())):
        order = list(map(int, input().split()))
        if order[0] == 1:
            heapq.heappush(list_, (-order[1], order[1]))
        elif order[0] == 2:
            if len(list_) != 0:
                result.append(heapq.heappop(list_)[1])
            else:
                result.append(-1)
    print(f"#{_}", end=" ")
    print(*result)
