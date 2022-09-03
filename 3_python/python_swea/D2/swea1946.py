import sys
sys.stdin = open('swea1946.txt')

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    word = ''
    print(f'#{_}')
    for a in range(N):
        x, y = input().split()
        for b in range(int(y)):
            word += x
            if len(word) == 10:
                print(word)
                word = ''
    if len(word) > 0:
        print(word)