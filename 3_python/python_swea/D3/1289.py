import sys
sys.stdin = open('1289.txt')

T = int(input())
for _ in range(1, T + 1):
    numbers = list(map(int, list(input())))
    switch = 1
    cnt = 0
    for a in range(len(numbers)):
        if numbers[a] == switch:
            switch = (switch + 1) % 2
            cnt += 1
    print(f'#{_} {cnt}')