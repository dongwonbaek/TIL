N = int(input())
star = '*'
add_star = ' *'
result = ''
for b in range(N):
    if b % 2 == 0:
        for a in range(N):
            if a % 2 == 0:
                if a == 0:
                    result += star
                elif a > 0:
                    result += add_star
            else:
                result += add_star
        print(result)
        result = ''
    else:
        for a in range(N):
            if a % 2 == 0:
                if a == 0:
                    result += add_star
                elif a > 0:
                    result += add_star
            else:
                result += add_star
        print(result)
        result = ''
