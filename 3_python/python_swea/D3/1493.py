import sys
sys.stdin = open('1493.txt')

T = int(input())
for _ in range(1, T + 1):
    p, q = map(int, input().split())
    result = [[]]
    x = 1
    y = 1
    i = 1
    for a in range(1, max(p, q) + 1):
        result.append([a, x, y])
        if y == 1:
            y += i
            i += 1
            x = 1
        else:
            x += 1
            y -= 1
    X = result[p][1] + result[q][1]
    Y = result[p][2] + result[q][2]
    answer = sum(list(range(X + Y - 1))) + X
    print(f'#{_} {answer}')