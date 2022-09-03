numbers = [0, 20, 100, 40, 120, -40]
a = numbers[0]
for b in numbers:
    if a < b:
        a = b

numberlist = list()
for b in numbers:
    if b < a:
        numberlist.append(b) 

c = numberlist[0]
for d in numberlist:
    if d > c:
        c = d
print(c)

# 모범 답안
# numbers = [0, 20, 100, 40]
# max_number = numbers[0]
# second_number = numbers[0]

# for n in numbers:
#     if max_number < n:
#         second_number = max_numbermax_number = n
#         print(second_number)