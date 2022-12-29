import sys
sys.stdin = open('1057.txt')

import math
N, kim, im = map(int, input().split())
cnt = 1
while True:
    if math.ceil(kim / 2) == math.ceil(im / 2):
        print(cnt)
        break
    else:
        kim = math.ceil(kim / 2)
        im = math.ceil(im / 2)
        cnt += 1