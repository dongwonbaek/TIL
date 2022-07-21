import sys
sys.stdin = open("SampleInput.txt", "r")

T = int(input())
for test_case in range(0, T + 1):
    if T != 0:
        print(T, end = ' ')
        T -= 1
    else:
        print(T)
        break