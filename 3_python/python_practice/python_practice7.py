a = [10, 1, 100]
new_a = a.sort()
print(a, new_a)
# [1,10, 100] None
# 리스트 메서드 활용
# 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경
# return되는 것은 None

b = [10, 1, 100]
new_b = sorted(b)
print(b, new_b)
# [10, 1,100] [1, 10, 100]
# 리스트에 sorted 함수를 활용
# sorted 함수를 활용하면, 원본을 변경하지 않음
# return 되는 것은 정렬된 리스트
