a = int(input())
if a < 0:
    a = -a
print(a)

num = -20
value = num if num >= 0 else -num
# 절대값 산출 코드이다. 규칙을 이해하는 것이 중요!
# value는 num이다. num이 0보다 크거나 같다면... 그게 아니라면 value에는 -num을 대입한다.