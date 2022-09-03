# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count) 

# 이 코드는 왜 결과 값이 다르게 나올까..
# 사람들은 문맥적으로 "a" or "e" .. 가 char와 같다라고 추론하지만,
# 파이썬 인터프리터는 원문 그대로 받아들인다.
# if (char == "a") or ("e") or ("i")  ...
# in 을 활용하거나 일일히 == 을 걸어줘야한다.

word = 'HappyHacking'

count = 0

for char in word:
    if char in 'aeiou':
        count += 1

print(count)
