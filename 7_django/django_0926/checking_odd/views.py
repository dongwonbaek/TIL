import random
from django.shortcuts import render

# Create your views here.
def checking_odd(request, number):
    if number == 0:
        text = "0"
    else:
        if number % 2 == 0:
            text = "짝수"
        else:
            text = "홀수"
    context = {
        "number": number,
        "text": text,
    }
    return render(request, "checking_odd/checking_odd.html", context)


def calculate(request, number_a, number_b):

    context = {
        "number_a": number_a,
        "number_b": number_b,
        "plus_": number_a + number_b,
        "minus_": number_a - number_b,
        "division_": number_a // number_b,
        "multiply_": number_a * number_b,
    }
    return render(request, "checking_odd/calculate.html", context)


def animal(request):

    return render(request, "checking_odd/animal.html")


def result(request):

    animal = [
        "말",
        "소",
        "개",
        "양",
        "호랑이",
        "고양이",
        "쥐",
        "닭",
        "용",
        "염소",
        "돼지",
        "뱀",
        "모기",
        "개미",
        "매미",
        "낙타",
        "코끼리",
        "기린",
        "사자",
        "다람쥐",
        "사람",
        "독수리",
        "오리",
        "백조",
        "지렁이",
        "공작",
    ]
    context = {"animal": random.choice(animal), "name": request.GET["name"]}
    return render(request, "checking_odd/result.html", context)


def lorem(request):
    return render(request, "checking_odd/lorem.html")


def ipsum(request):
    random_name = [
        "짜장면 ",
        "탕수육 ",
        "짬뽕 ",
        "육개장 ",
        "배고프다 ",
        "놀고싶다 ",
        "핸드폰 ",
        "컴퓨터 ",
        "키보드 ",
        "마우스 ",
        "이어폰 ",
        "마이크 ",
        "코카콜라 ",
    ]
    num_paragraph = request.GET["num_paragraphs"]
    num_word = request.GET["num_words"]
    result2 = []
    for b in range(int(num_paragraph)):
        result1 = ""
        for a in range(int(num_word)):
            result1 += random.choice(random_name)
        result2.append(result1)
    context = {
        "result": result2,
    }
    return render(request, "checking_odd/ipsum.html", context)


def root(request):
    return render(request, "checking_odd/root.html")
