import sys
sys.stdin = open('2304.txt')

max_ = 0
height = 0
result = []
min_ = 1000
N = int(input())
for _ in range(N):
    L, H = map(int, input().split())
    result.append((L, H))
    if L > max_:
        max_ = L
    if H > height:
        height = H

chango = [0] * (max_ + 1)
for a in result:
    chango[a[0]] = a[1]
    if a[0] < min_:
        min_ = a[0]
    
area = 0
highest = 0
highest_ = 0
cnt1 = 0
cnt2 = 0
cnt = 0
cnt_ = 0

for b in range(min_, len(chango)):
    if chango[b] > highest:
        area += ((cnt2) * highest)
        highest = chango[b]
        cnt1 += cnt2
        cnt2 = 0
    cnt2 += 1

for c in range(len(chango) - 1, -1, -1):
    if chango[c] > highest_:
        area += (cnt_ * highest_)
        highest_ = chango[c]
        cnt += cnt_
        cnt_ = 0
    cnt_ += 1
area += (height * (max_ - min_ - cnt - cnt1 + 1))
print(area)