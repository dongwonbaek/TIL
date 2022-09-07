import sys
sys.stdin = open('2559.txt')

# N, K = map(int, input().split())
# dayz = list(map(int, input().split()))
# result = -100
# for a in range(len(dayz) - K + 1):
#     answer = 0
#     for b in range(K):
#         answer += dayz[a]
#         a += 1
#     if answer > result:
#         result = answer
# print(result)
# 시간 초과

N, K = map(int, input().split())
dayz = list(map(int, input().split()))
answer = 0
for a in range(K):
    answer += dayz[a]
result = answer
b = 0
while b < N - K:
    next_stage = answer - dayz[b] + dayz[b + K]
    if (next_stage) > result:
        answer = next_stage
        result = answer
    else:
        answer = next_stage
    b += 1
print(result)