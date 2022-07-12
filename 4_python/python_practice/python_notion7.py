numbers = [0, 20, 100]
a = numbers[0]
for b in numbers:
    if b < a:
        a = b
print(a)