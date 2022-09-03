T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    fast = 0
    distances = 0
    for a in range(N):
        list_ = list(map(int, input().split()))
        if list_[0] == 1:
            fast += list_[1]
            distances += fast
        elif list_[0] == 2:
            fast -= list_[1]
            if fast < 0:
                fast = 0
            distances += fast
        else:
            distances += fast
    print(f'#{_} {distances}')