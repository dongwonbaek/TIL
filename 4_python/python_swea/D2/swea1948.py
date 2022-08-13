import sys
sys.stdin = open('swea1948.txt')
n = int(input())
m = int(input())
matrix = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
distances = [0] * (n + 1)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    matrix[x].append((y, z))
start, arrive = map(int, input().split())
check[start] += 1

stack = [(start, 0)]
while len(stack) != 0:
    cur = stack.pop()
    for a in matrix[cur[0]]:   
        stack.append(a)
        if check[a[0]] < check[cur[0]] + 1:
            check[a[0]] = check[cur[0]] + 1
        if distances[a[0]] < distances[cur[0]] + a[1]:
            distances[a[0]] = distances[cur[0]] + a[1]

print(distances[arrive])
print(check[arrive])    