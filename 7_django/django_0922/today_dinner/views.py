from django.shortcuts import render
import random
# Create your views here.
def dinner(request):
    menu_name = [
        ('짜장면', 'http://cdn.kormedi.com/wp-content/uploads/2021/10/r658x041.jpg'),
        ('짬뽕', 'https://img.siksinhot.com/article/1637897338299104.jpg'),
        ('평양냉면', 'https://blog.kakaocdn.net/dn/bAMlNq/btrdV6GiSKD/LzyXr8bQpZwWpQcw2tPkK1/img.jpg'),
        ('함흥냉면', '//thumbnail10.coupangcdn.com/thumbnails/remote/492x492ex/image/vendor_inventory/c4dc/41f109ce047921c7781722e9b4f8b2519a7526cc8a7e1e968348ac0a20ea.jpg'),
        ('바지락칼국수', 'https://mp-seoul-image-production-s3.mangoplate.com/651394_1576772075670405.jpg?fit=around|738:738&crop=738:738;*,*&output-format=jpg&output-quality=80'),
        ('들깨칼국수', '//image.auction.co.kr/itemimage/1b/11/f9/1b11f93d06.jpg'),
        ('오일파스타', 'https://sitem.ssgcdn.com/51/92/02/item/2097001029251_i1_1200.jpg'),
        ('토마토파스타', '//cdn.mariooutlet.com/Product/A0560/C1N/P001437953_d1.jpg?AR=0&RS=520X660'),
        ('잔치국수', 'http://www.palnews.co.kr/news/photo/201712/91750_24575_1653.jpg'),
        ]
    random_number = random.randrange(len(menu_name))

    context = {
        'name': menu_name[random_number][0],
        'img': menu_name[random_number][1],
    }
    return render(request, 'today_dinner.html', context)

def lotto(request):
    context = dict()
    win = [3, 11, 15, 29, 35, 44]
    bonus_win = 10
    for a in range(5):
        cnt = 0
        switch = False
        result = random.sample(range(1, 46), 7)
        bonus = result.pop()
        context[f'sample_{a + 1}'] = result
        context[f'bonus_{a + 1}'] = bonus
        for b in result:
            if b in win:
                cnt += 1
            if b == bonus_win:
                switch = True
        if cnt == 3:
            rate = 5
        elif cnt == 4:
            rate = 4
        elif cnt == 5 and switch == False:
            rate = 3
        elif cnt == 5 and switch == True:
            rate = 2
        elif cnt == 6:
            rate = 1
        else:
            rate = 0
        context[f'rate_{a + 1}'] = rate
    return render(request, 'lotto.html', context)

def fake(request):
    context = {
        
    }
    return render(request, 'fake_naver.html', context)