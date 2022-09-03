N = int(input())

hansu = []

if N >= 100:
    for a in range(100, N + 1):
        cnt = 0
        numbers = a
        number_list = []
        while a != 0:
            number_list.append(a % 10)
            a //= 10
        for b in range(1, len(str(numbers)) - 1):
            v_cost = number_list[0] - number_list[1]
            if v_cost == number_list[b] - number_list[b + 1]:
                cnt += 1
                if cnt == (len(str(numbers)) - 2):
                    hansu.append(numbers)
                    break
            else:
                break    
        
    print(len(hansu) + 99)       

else:
    print(N)