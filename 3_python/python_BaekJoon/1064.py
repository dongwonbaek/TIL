import sys
sys.stdin = open('1064.txt')

import math
xa, ya, xb, yb, xc, yc = map(int, input().split())

a = xa - xb
b = ya - yb
c = a * ya - b * xa

if a * yc - b * xc == c:
    print(-1)
else:
    result = []
    result.append((math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2) + math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)) * 2)
    result.append((math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2) + math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)) * 2)
    result.append((math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2) + math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)) * 2)
    print(max(result) - min(result))