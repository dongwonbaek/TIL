import sys
sys.stdin = open('2564.txt')

start_dir = [2, 1, 4, 3]
X, Y = map(int, input().split())
N = int(input())
result = 0
sampling = []
for i in range(N):
    x, y = map(int, input().split())
    if x == 1:
        b = Y
        a = y
    elif x == 2:
        b = 0
        a = y
    elif x == 3:
        a = 0
        b = Y - y
    elif x == 4:
        a = X
        b = Y - y
    sampling.append((x, a, b))

x, y = map(int, input().split())
opposite = start_dir[x - 1]
if x == 1:
    b = Y
    a = y
elif x == 2:
    b = 0
    a = y
elif x == 3:
    a = 0
    b = Y - y
elif x == 4:
    a = X
    b = Y - y
dong = (x, a, b)
for j in sampling:
    if j[0] != opposite:
        result += (abs(j[1] - dong[1]) + abs(j[2] - dong[2]))
    else:
        if x == 1 or x == 2:
            result += min(dong[1] + j[1] + Y, (2 * X + 2 * Y) - (dong[1] + j[1] + Y))
        else:
            result += min(Y - dong[2] + Y - j[2] + X, (2 * X + 2 * Y) - (Y - dong[2] + Y - j[2] + X))
print(result)