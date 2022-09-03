import requests

# 내가 고른 숫자 6자리로 이제껏 진행된 로또 추첨 1024회 동안 1등을 하여 얼마를 받을 수 있을까?

n = 1
url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
b = list(map(int,input('1부터 45까지 6개의 숫자를 고르시오(중복x)').split()))
response = requests.get(url).json()
number_list = [response.get('drwtNo1'), response.get('drwtNo2'), response.get('drwtNo3'), response.get('drwtNo4'), response.get('drwtNo5'), response.get('drwtNo6')]
win_price = 0

for a in range(1,1025):
    n = a
    if set(b) in set(number_list):
        win_price += response.get('firstWinamnt')

print(win_price)
# 원하는 값이 출력되지 않는다. 고민을 좀 더 해봐야겠다.