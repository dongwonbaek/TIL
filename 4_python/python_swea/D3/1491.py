import sys
sys.stdin = open('1491.txt')

T = int(input())
for _ in range(1, T + 1):
    N, A, B = map(int, input().split())
    result = []
    a = 1
    while True:
        if (a + 1) ** 2 > N:
            break
        else:
            a += 1
    for R in range(1, a + 1):
        C = 1
        while True:
            if R * C <= N:
                result.append(A*abs(R-C) + B*(N-R*C))
                C += 1
            else:
                break
    print(f'#{_} {min(result)}')