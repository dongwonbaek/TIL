first_numbers = range(2, 10)
second_numbers = range(1, 10)

for a in first_numbers:
    print(a,'단')
    for b in second_numbers:
        print(a, 'X', b, '=', a*b)