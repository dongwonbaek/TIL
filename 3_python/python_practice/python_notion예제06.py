# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# .append 메소드는 리스트에 적용가능한 메소드이다.
# answer = () 는 빈 튜플을 선언하는 것이므로 ()이 아닌 []로 변경하는 것이 옳다.
# 또한 range(N+1)은 0부터 N까지 나열하기 때문에 1부터 N까지로 변경하기 위해서는 
# range(1, N + 1)로 구간을 정해주는 것이 옳다.

N = 10
answer = []
for number in range(1, N + 1):
    answer.append(number * 2)

print(answer)