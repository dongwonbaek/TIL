import sys

sys.stdin = open("2948.txt")

for _ in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    list_A = input().split()
    list_B = input().split()
    cnt = 0
    for a in list_A:
        for b in list_B:
            if a == b:
                cnt += 1
                break
    print(f"#{_} {cnt}")
