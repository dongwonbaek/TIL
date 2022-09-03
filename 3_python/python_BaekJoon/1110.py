N = int(input())
cnt = 0
real_number = N

while True:
    number = N
    number_list = []
    while number != 0:
        number_list.append(number % 10)
        number //= 10
    new_number = (N % 10) * 10 + (sum(number_list) % 10)
    cnt += 1
    if new_number == real_number:
        print(cnt)
        break
    else:
        N = new_number