import sys
sys.stdin = open('1049.txt')

N, M = map(int, input().split())
six = 0
one = 0
for a in range(M):
    A, B = map(int, input().split())
    if a == 0:
        if B * 6 < A:
            A = B * 6
        six = A
        one = B
    else:
        if B * 6 < A:
            A = B * 6
        if six > A:
            six = A
        if one > B:
            one = B
share = N // 6
remain = N % 6
if six < remain * one:
    share += 1
    print(share * six)
else:
    print((share * six) + (remain * one))