import sys
sys.stdin = open('1220.txt')

for _ in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for z in range(100)]
    check = [[False] * 100 for x in range(100)]
    cnt = 0
    for a in range(100):
        for b in range(100):
            if matrix[b][a] == 1 and check[b][a] == False:
                for c in range(b + 1, 100):
                    if matrix[c][a] == 2:
                        cnt += 1
                        check[c][a] = True
                        check[b][a] = True
                        break
                    elif matrix[c][a] == 1:
                        break
            if matrix[99 - b][a] == 2 and check[99 - b][a] == False:
                for c in range(98 - b, -1, -1):
                    if matrix[c][a] == 1:
                        cnt += 1
                        check[c][a] = True
                        check[99 - b][a] = True
                        break
                    elif matrix[c][a] == 2:
                        break
    print(f'#{_} {cnt}')