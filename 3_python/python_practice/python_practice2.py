print('미세먼지 농도를 입력하세요.')
a = int(input())
if a > 150:
    print('매우나쁨')
elif a > 80:
    print('나쁨')
elif a > 30:
    print('보통')
else:
    print('좋음')