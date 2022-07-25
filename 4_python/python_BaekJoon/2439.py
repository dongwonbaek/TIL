# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

N = int(input())
star = '*'
stars = ''
space = ' '
for a in range(1, N + 1):           # 1에서 N까지 순차적으로 할당
    for n in range(1,(N - a + 1)):  # 최대 별의 개수 - a 로 공백이 들어갈 횟수를 결정한다.
        stars += space              # 결정된 횟수만큼 공백을 넣는다.
    for i in range(1, a + 1):       # 그 후 별이 들어갈 횟수를 결정하고
        stars += star               # 별을 추가한다.
    print(stars)
    stars = ''                      # stars 를 초기화한다.