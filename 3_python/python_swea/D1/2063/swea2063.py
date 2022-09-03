import sys
sys.stdin = open("input.txt", "r")

T = int(input())
a = list(map(int,input().split()))
a.sort()
print(a[round(len(a)/2)-1])