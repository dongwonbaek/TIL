# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count += 1 의 위치가 부적절하다. number_list에 존재하는 숫자가 더해질 때마다 1씩 추가되어야 하는데,
# 현재 count의 위치는 for문이 종료된 후에 1을 더하는 것으로, count가 1의 값만 가지고 전체 합을 나누게 된다.
# 또한 //은 나누기가 아닌 몫을 구하는 것으로 평균을 구하기 위해서는 부적절하다. /을 사용해야 한다.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)