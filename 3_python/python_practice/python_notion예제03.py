# numbers = input().split()
# print(sum(numbers))

# input 함수는 기본적으로 문자열에 해당한다.
# 그렇기 때문에 sum 함수를 사용하여 합을 구하기 위해서는 
# 입력받은 값을 모두 정수형, int로 변환 후에 sum을 적용해야 한다.

numbers = map(int,input().split())
print(sum(numbers))