# while 문을 활용하여 1부터 인풋값까지 모두 곱하기
# a = int(input())
# b = 1
# result = 1
# while b <= a:
#     result *= b
#     b += 1
# print(result)

# for 문을 활용하기
a = int(input())
result = 1
for b in range(a):
    result *= (b+1)
print(result)