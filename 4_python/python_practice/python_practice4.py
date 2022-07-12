a = int(input())
total = int((a+1)*a/2)
print(total)

n = 0
result = 0
user_input = int(input())
while n < user_input:
    print(f'n: {n}, result: {result}') # 진행과정을 확인하는 코드
    result += n
    n += 1
print(result)
# 1부터 입력값까지 더하는 코드
