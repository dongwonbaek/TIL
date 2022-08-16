import sys
sys.stdin = open('swea1959.txt')

T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    a = 0
    result = []
    if N > M:
        while a + M <= N:
            number_list = []
            for b in range(a, a + M):
                number_list.append(Ai[b])
            result_number = 0
            for c in range(M):
                result_number += (number_list[c] * Bj[c])
            result.append(result_number)
            a += 1
        print(f'#{_} {max(result)}')
    else:
        while a + N <= M:
            number_list = []
            for b in range(a, a + N):
                number_list.append(Bj[b])
            result_number = 0
            for c in range(N):
                result_number += (number_list[c] * Ai[c])
            result.append(result_number)
            a += 1
        print(f'#{_} {max(result)}')
