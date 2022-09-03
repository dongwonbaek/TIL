import sys
sys.stdin = open('swea2007.txt')

T = int(input())
for _ in range(1, T + 1):
    word = input()
    sampling = ''
    for a in range(10):
        sampling += word[a]
        wording =''
        while len(wording) != 30:
            for a in sampling:
                wording += a
                if len(wording) == 30:
                    break
        if word == wording:
            print(f'#{_} {len(sampling)}')
            break