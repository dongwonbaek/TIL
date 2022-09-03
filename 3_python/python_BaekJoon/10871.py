N, X = map(int, input().split())
N_list = list(map(int, input().split()))

for i in N_list:
    if i < X:
        print(i, end = ' ')