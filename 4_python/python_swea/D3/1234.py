import sys
sys.stdin = open('1234.txt')

for _ in range(1, 11):
    amnt, number = input().split()
    number_list = list(number)
    switch = True
    result = ''
    while switch == True:
        for a in range(len(number_list)-1):
            original = len(number_list)
            if number_list[a] == number_list[a + 1]:
                number_list.pop(a)
                number_list.pop(a)
                break
        if len(number_list) == original:
            switch = False
    for b in number_list:
        result += b
    print(f'#{_} {result}')