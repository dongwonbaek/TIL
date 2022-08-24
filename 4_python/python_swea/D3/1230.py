import sys
sys.stdin = open('1230.txt')

for _ in range(1, 11):
    N = int(input())
    original = input().split()
    order_amnt = int(input())
    order = input().split()
    for a in range(len(order)):
        number_list = []
        if order[a] == 'I':
            x = int(order[a + 1])
            y = int(order[a + 2])
            for b in range(a + 3, a + 3 + y):
                original.insert(x, order[b])
                x += 1
        elif order[a] == 'D':
            x = int(order[a + 1])
            y = int(order[a + 2])
            for h in range(y):
                original.pop(x)
        elif order[a] == 'A':
            y = int(order[a + 1])
            for g in range(a + 2, a + 2 + y):
                original.append(order[g])
    print(f'#{_}', end = ' ')
    for d in range(10):
        print(original[d], end = ' ')
    print()
