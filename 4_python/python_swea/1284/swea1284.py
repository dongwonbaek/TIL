import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    P, Q, R, S, W = map(int,input().split())
    priceA = P * W

    if W <= R:
        priceB = Q
    else:
        priceB = Q + ((W - R) * S)
        
    if priceA <= priceB:
        print(f'#{test_case} {priceA}')
    else:
        print(f'#{test_case} {priceB}')

    