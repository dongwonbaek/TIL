# T = int(input())
# for _ in range(1, 1 + T):
#     len_numbers = int(input())
#     number_list = list(map(int, input().split()))
#     sum_final = 0
#     sum_ = []

#     for b in range(len_numbers - 1):
#         if number_list[b] <= number_list[b + 1]:
#             sum_.append(number_list[b + 1] - number_list[b])
#             if b == len_numbers - 2:
#                 for c in range(len(sum_)):
#                     sum_final += sum_[c] * (c + 1)
#         else:
#             for c in range(len(sum_)):
#                 sum_final += sum_[c] * (c + 1)
#             sum_ = []
#     print(f'#{_} {sum_final}')
# 오답입니다. 런타임 에러 발생. 시간복잡도를 줄여야 함.

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    biggest = 0
    sum_ = 0
    for a in num_list[::-1]:
        if a > biggest:
            biggest = a
        else:
            sum_ += (biggest - a)
    print(f'#{_} {sum_}')