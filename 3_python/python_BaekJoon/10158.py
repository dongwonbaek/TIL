import sys
sys.stdin = open('10158.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x = t % (2 * w)
y = t % (2 * h)
if x <= w - p:
    p += x
elif w - p < x < 2 * w - p:
    p = w - (x - (w - p))
else:
    p = x - (w - p) - w

if y <= h - q:
    q += y
elif h - q < y < 2 * h - q:
    q = h - (y - (h - q))
else:
    q = y - (h - q) - h

print(p, q)
# move_dir = [1, 1]
# cnt = 1
# while cnt <= t:
#     if 0 <= p + move_dir[0] <= w and 0 <= q + move_dir[1] <= h:
#         p += move_dir[0]
#         q += move_dir[1]
#         cnt += 1
#     else:
#         if (p + move_dir[0] < 0 or p + move_dir[0] > w) and 0 <= q + move_dir[1] <= h:
#             move_dir[0] *= -1
#         elif 0 <= p + move_dir[0] <= w and (q + move_dir[1] < 0 or q + move_dir[1] > h):
#             move_dir[1] *= -1
#         elif (p + move_dir[0] < 0 or p + move_dir[0] > w) and (q + move_dir[1] < 0 or q + move_dir[1] > h):
#             move_dir[0] *= -1
#             move_dir[1] *= -1
# print(p, q)

