a = int(input())
if a % 2 == 0 and a < 0:
    print('A')
if a % 2 != 0 and a < 0:
    print('B')
if a % 2 == 0 and a > 0:
    print('C')
if a % 2 != 0 and a > 0:
    print('D')