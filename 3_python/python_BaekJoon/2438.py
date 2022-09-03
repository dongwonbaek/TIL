# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

N = int(input())
star_list = []
star = '*'
stars = '*'
for star_number in range(N):
    star_list.append(stars)
    print(stars)
    stars += star
    
