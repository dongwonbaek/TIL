# Django

#### Framework 란?

다양한 개발에 사용되는 코드 부분들을 재사용할 수 있게 좋은 구조의 코드로 만들어 두고, 그러한 코드들을 모아 놓은 것, 즉 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것이다.

Framework를 잘 사용하기만 한다면 서비스 개발에 있어서 하나부터 열까지 개발할 필요가 없게 되어, 본질적으로 집중할 수 있고, 시간과 노력을 많이 아낄 수 있다.

클라이언트 측 Framework(Bootstrap)는 개발하는 속도를 올려줄 수 있지만 모든 코드를 직접 작성할 수도 있다. ( 그게 더 나을 때도 있을 것이다.) 하지만 서버 측 Framework(Django)을 직접 작성하는 것은 매우 비효율적일 뿐만아니라 완성도 측면에서도 많이 떨어질 수 있기 때문이다.



#### Django 란?

Python으로 작성된, 서버를 구현하는 웹 Framework이다. 

클라이언트에서 요청된 URL을 HTML문서로 응답하는 서버이다.

Python이라는 언어의 강력함과 거대한 커뮤니티가 만나 수많은 유용한 기능들을 제공하고, Toss, 당근마켓, 요기요 등 거대 기업들이 현재 Django를 활용하고 있음



#### 클라이언트와 서버 란?

- 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작
  - 클라이언트

    - 웹 사용자의 인터넷에 연결된 장치
    - Chrome 또는 Firefox와 같은 웹 브라우저
    - 서비스를 요청하는 주체

  - 서버

    - 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터

    - 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨

    - 요청에 대해 서비스를 응답하는 주체

- Google 홈페이지에 접속한다는 것은 밑의 과정이 이루어진다는 것을 의미한다.
  1. 인터넷으로 연결된 Google 서버에 Google 홈페이지.html 파일을 달라고 요청하고,
  2. Google 서버는 우리의 요청을 받고 인터넷을 통해 html 파일을 전송하고,
  3. 컴퓨터의 브라우저는 받은 html 파일을 우리가 볼 수 있도록 해석하여 표현한다.



#### 웹 브라우저 란?

- 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
- 웹페이지 파일을 우리가 보는 화면으로 바꿔주는(렌더링, rendering) 프로그램
- HTML / CSS / JS 로 구성된 HTML 문서파일을 우리가 보는 예쁜 화면으로 구성해주는 프로그램



#### 웹 페이지 란?

- 우리가 보는 화면 각각 한 장 한 장이 웹 페이지
- 정적 웹 페이지와 동적 웹 페이지가 있음
- 정적 웹 페이지(Static Web page)
  - 있는 그대로를 제공하는 것으로, 한 번 작성된 HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것
  - 같은 상황에서 모든 사용자에게 동일한 정보를 표시
- 동적 웹 페이지(Dynamic Web page)
  - 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
    - 개별 사용자에 맞게 정보를 효율적으로 전달할 수 있게 해주고 사용자 경험을 훨씬 향상시킬 수 있음.
    - 예를 들어, 고객선호도와 이전 구매 습관을 기반으로 한 제품 제안, 재미있는 컨텐츠에 대한 액세스를 강조하고 공유할 수 있음.
  - 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌.
  - Django 가 이런 동작 웹 페이지를 쉽게 만들 수 있게 도와줌.
  - 다양한 서버 사이드 프로그래밍 언어(python, java, c++) 를 사용하여 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐



#### URL의 구조

URI : http://www.naver.com:80/~~~

- 누구에게 : naver에게
- 무엇을 : ~~~을 주문한다.
- 기본은 / (root페이지) 를 주문한다.



### 브라우저에 웹 주소를 입력할 때 어떤 일이 일어날까?



1. **브라우저는 DNS 서버로 가서 웹사이트가 있는 서버의 진짜 주소를 찾습니다.**

   

2. **브라우저는 서버에게 웹사이트의 사본을 클라이언트에게 보내달라는 HTTP 요청 메세지를 서버로 전송합니다.**  

   *(이 때 메세지, 클라이언트와 서버 사이에 전송된 모든 데이터는 TCP/IP 연결을 통해 전송됩니다.)*

   

3. **이 메세지를 받은 서버는 클라이언트의 요청을 승인하고, "200 OK" 메세지를 클라이언트에게 전송합니다.** 

   *(이 때 "200 OK"는 "물론이죠, 당신은 웹 사이트를 볼 수 있습니다. 보내드릴게요." 라는 의미입니다. )*

   

4. **그 다음 서버는 웹사이트의 파일들을 데이터 패킷이라 불리는 작은 일련의 덩어리들로 브라우저에 전송하기 시작합니다.**

   

5. **브라우저는 이 작은 덩어리들을 완전한 웹 사이트로 조립하여 보여줍니다.**



#### DNS (Domain Name System Servers)

실제 웹 주소는 63.245.217.105 와 같은 숫자 덩어리이기 때문에 쉽게 기억할 수 없습니다. 

DNS 는 브라우저에 입력하는 웹 주소(google.com)를 실제 (IP) 주소와 맞춰주는 특별한 서버입니다.



### **가상환경 생성,실행 및 Django를 통해 서버 생성**

가상환경을 생성할 폴더로 이동 후 깃 배쉬 실행

가상환경(venv)은 프로젝트별로 활용하는 툴의 버전, 종류가 다르기 때문에 활용툴을 컨트롤하기 위하여 사용한다.



1. **server-venv라는 가상환경이름으로 가상환경구성폴더 생성, 이 때 venv는 파이썬의 가상환경 모듈이다.**

   ~~~bash
    $ python -m venv server-venv
   ~~~

   

2. **가상환경 실행**

   ~~~bash
   $ source server-venv/Scripts/activate
   
   # 가상환경 종료
   $ deactivate
   ~~~

   

3. **장고 설치**

   ~~~bash
   $ pip install django==3.2.13
   ~~~
   `버전 명시는 == , 장고의 가장 안정적인 버전이 3.2.13(LTS)버전`

   `LTS (Long Term Support) : 장기 지원 버전`

   ~~~bash
   # 현재 적용되어있는 pip 프로그램들의 이름을 requirements.txt라는 메모장에 저장하여 공유하기 쉽게 한다.
   $ pip freeze > requirements.txt
   
   # 다음 명령어를 통해 적용할 수 있다. 이 때 requirements.txt 파일은 가상환경	(venv) 폴더 내에 있어야 한다.
   $ pip install -r requirements.txt
   ~~~





4. **프로젝트 생성**

   ~~~bash
   $ django-admin startproject [프로젝트이름] [시작경로]
   ~~~
   
   
      `시작경로에 현재폴더를 지정하고 싶으면 . 을 입력하면 된다.`



5. **현재 폴더를 vs code로 오픈하여 확인**

   ~~~bash
   $ code .
   ~~~




6. **장고 설치 시 생성된 manage.py를 실행하여 내 컴퓨터에만 존재하는 서버 실행**

   ~~~bash
   $ python manage.py runserver
   # 실행하기 전에 ls를 입력하여 manage.py 파일이 현재 경로에 존재하는지 확인
   ~~~




7. **브라우저에 localhost:8000 입력**

   장고에서 웹페이지를 성공적으로 생성했다는 페이지 출력



8. **어플 생성**

   ~~~bash
   $ python manage.py startapp articles
   ~~~

   

9. **어플 등록**

    프로젝트폴더 안에 settings.py 안에 INSTALLED_APPS 라는 이름의 리스트 안에 최상단에 어플 폴더를 넣는다. ('articles' ,<-- 이렇게 넣는다.)

    

10. **요청과 응답 설계**

    1. 주문서 정의 (urls.py)
    2. 로직 구현 (views.py)
    3. HTML 페이지 구성 (~~~.html)

    

11. **URL 선언**

    urls.py 파일의 ulrpatterns 라는 리스트에 path('index/', views.index), 를 추가한다.

    ~~~python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index), 
    ]
    # views.py 내의 index()함수를 실행하고, 경로는 index/로 한다.
    # 만약 경로를 비워놓는다면('') root주소가 지정된다(메인홈페이지).
    ~~~


​    

12. **views.py 파일에서 어떤 내용을 불러올 것인지에 대한 정보를 삽입**

    ~~~python
    # views.py
    
    from django.shortcuts import render
    
    def index(request):
        number = 1
        context = {
            "num": number,
            "num2": number,
        }
        return render(request, "index.html", context)
    ~~~
    
    

13. **앱 내부에 templates 폴더 생성 (templates 이름은 변경하지 않는다.)**

    templates 폴더는 웹사이트를 구성하는 HTML 문서들이 저장되는 공간이다.

    13번에서 index라는 함수가 index.html 문서를 반환하게 작성했으므로 templates 폴더에 index.html을 작성한다.

    

14. **html에서 파이썬 활용하기 (Django 한정)**
    
    ~~~html
    <body>
        <!-- for문 -->
        {% for number in numbers %}
        <p>{{ number }}</p>
        {% endfor %} 
     	<!-- 기존 파이썬과는 조금 다르게 구문 종료를 명시해야함-->
        
        <!-- if문 -->
        {% if number > 0 %}
        <p>{{ number }}</p>
        {% endif %}
    </body>
    ~~~



### Variable routing

- URL 주소를 변수를 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

- 변수는 '<>' 에 정의하여 view 함수의 인자로 할당됨

- 기본 타입은 string이며 5가지 타입으로 명시할 수 있음

  - str

  - int

  - slug

  - uuid

  - path

   ~~~python
    # urls.py
    urlpatterns = [
        path('hello/<str:name>/', views.hello),
    ]
    
    # views.py
    def hello(request, name):
        context = {
            'name': name,
        }
        return render(request, 'hello.hetml', context)
   ~~~

   ~~~html
    <!-- templates/hello.html -->
    <h1>
        만나서 반가워요 {{ name }} 님!
    </h1>
   ~~~




### 템플릿 상속

- 모든 템플릿에 공통적으로 부트스트랩을 적용시킨 기준 템플릿을 만들 수 있을까?

~~~html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    {% block content %}
    {% endblock content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</body>
</html>
~~~

~~~html
<!-- base.html을 활용한 다른 html파일 -->
{% extends 'base.html' %}
<!-- extends 는 템플릿 최상단 폴더를 기준으로 한다. -->
{% block content %}
	<h1>
        안녕하세요~
	</h1>
{% endblock %}
<!-- content는 다른 이름으로 대체할 수 있고 그렇기 때문에 여러 블럭을 지정할 수도 있다. -->
~~~

~~~python
# pjt/settings.py
# 기본 템플릿양식 경로 설정
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"], # 기본 템플릿 양식의 위치를 알려준다.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
~~~



#### URL 분할

- 프로젝트 내 앱의 view 함수가 많아지면서 사용하는 path() 함수가 많아지고, 앱 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않다.

- 하나의 프로젝트에 여러 앱들이 존재한다면, 각각의 앱 안에 urls.py를 만들고 프로젝트 urls.py 에서 각 앱의 urls.py 파일로 URL 을 맵핑할 수 있음

  ~~~python
  # 앱 urls.py
  from django.urls import path
  from . import views 
  # 현재 위치에 있는 views.py 파일을 참조한다.
  
  urlpatterns = [
      path('index/', views.index),
      path('greeting/', views.greeting),
  ]
  ~~~

- 이 때 프로젝트 urls.py 내에는 path 와 같은 경로의 include 모듈을 import 해야 함

  ~~~python
  # 프로젝트 urls.py
  from django.contrib import admin
  from django.urls import path, include 
  # include는 django.urls 파일에 내장되어있는 모듈이다.
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('pages/', include('pages.urls')),
  ]
  ~~~

- 프로젝트 urls에서 관리하던 path가 분리되었으므로, URL 주소 또한 바뀌게 됨.

  `기존이 http://localhost:8000/index/ 였다면 현재는 http://localhost:8000/articles/index/`



#### URL Namespace

- path 함수 내에 name 속성을 추가하여 templates 에서 특정양식`{% url '[app_name]:[name]' %}`을 통해 호출할 수 있다.

- 앱 urls.py 에 app_name 을 지정하여 여러 앱들 간에 혼동을 없앨 수 있고, 절대경로를 통해 유지보수 또한 편리해진다.

  ~~~python
  # articles/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  urlpatterns = [
      path('index/', views.index, name='index'),
      path('greeting/', views.index, name='greeting'),
      # name 속성에 활용할 절대변수를 할당한다.
  ]
  ~~~

  ~~~html
  <!-- articles/templates/index.html -->
  {% block content %}
  <h1>만나서 반가워요</h1>
  <a href="{% url 'articles:greeting' %}">greeting</a>
  {% endblock %}
  ~~~






POST

- form 태그 뒤 method 의 기본값은 GET이다.
- POST로 변경하면 form 태그의 역할이 바뀌게 된다.
- GET은 조회하기 위해 조회대상의 정보를 URL에 담아 전송했다면, POST는 데이터베이스에 등록하기 위해 등록할 정보를 메시지에 담아 전송한다.
- POST를 활용하기 위해서는 반드시 form 태그 내부에 {% csrf_token %} 을 추가해야함(보안 유지)



하나의 메서드에 두 가지 기능을 추가하기.

if 문으로 method가 post냐 get이냐 를 판별하고 기능을 각자 작성한다.

유효성 검사에서 탈락할 경우 상황도 생각해야 함



### ModelForm

- 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며 이는 서버 사이드에서 반드시 처리해야 함
- ModelForm은 Model에 정의된 필드에 맞춰
  - UI를 자동으로 그려주고
  - 유효성을 검사하고
  - DB에 저장한다.
- ModelForm은 Form과 똑같은 방식으로 View함수에서 사용



#### ModelForm 선언

~~~python
# articles/forms.py
from django import forms # forms 라이브러리의 ModelForm 클래스를 상속받음
from .models import Article 

class ArticleForm(forms.ModelForm):
    
    
    class Meta: 			# 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
        model = Article 	# ModelForm이 참조할 모델을 정의       
        fields = '__all__' 	# __all__을 활용하여 참조할 모델의 모든 필드를 포함할 수 있음
      #	fields = ['title', 'content']	# 또는 원하는 필드만 선택할 수도 있음
	  #	exlclude = ('title',) 	# exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정가능
~~~

#### ModelForm 활용

~~~python
# articles/views.py
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
	# ModelForm 객체를 context에 담아서 전달
~~~

~~~html
<!-- articles/new.html -->
{% extends 'base.html' %}

{% block content %}
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}	<!-- 유효성 검사 -->
    {{ form.as_p }}		<!-- context로 전달받은 객체를 어떤 방식(as_p)으로 출력할 것인지 표현 -->
    <input type="submit">
</form>
{% endblock content %}
~~~

##### label 과 input 쌍에 대한 3가지 출력 옵션

- as_p 
  - 각 필드가 단락(p 태그)으로 감싸져서 랜더링
- as_ul
  - 각 필드가 목록(li 태그)으로 감싸져서 랜더링
  - ul 태그는 직접 작성해야 함
- as_table
  - 각 필드가 테이블(tr 태그) 행으로 감싸져서 랜더링



#### 기능 합치기(Create, Update)

- Create

~~~python
# articles/views.py
from django.shortcuts import render, redirect
from .forms import ArticleForm # 유효성 검사를 위해 선언했던 ModelForm 참조

def create(request):
    if request.method == 'POST':	# 만약 request로 날라온 요청(내용이 담긴)이 POST 방식이라면,
        form = ArticleForm(request.POST)	# 그 내용을 ModelForm에 담고,
        if form.is_valid():			# 유효성 검사에 통과하면,
            article = form.save()	# 그 내용을 DB에 반영하고,
            return redirect('articles:detail', article.pk) # detail로 바로 연결(pk를 담아서)
        # 만약 유효하지 않다면? 저장되지 않고 아무일도 일어나지 않음.
        
    else:							# 요청방식이 POST가 아나라 GET 이라면?
        form = ArticleForm()		
	context = {						# 유효성 검사에 통과하지 못했을 경우 여기로 점프하여 에러메시지가 담긴 form을 할당
        'form': form,
    }
    return render(request, 'articles/create.html', context)	# 에러메시지와 함께 create.html을 재출력
~~~



- Update (edit 기능과 합치기)

~~~python
# articles/views.py
from django.shortcuts import render, redirect
from article.models import Article
from .forms import ArticleForm 	# 유효성 검사를 위해 선언했던 ModelForm 참조

def update(request, pk):
	article = Article.objects.get(pk=pk) 	# Update(편집)는 instance에 사용할 객체를 미리 할당하는 것이 좋다.
	if request.method == 'POST':			# 만약 날라온 요청이 POST 방식이라면, 날라온 데이터를 검사한다.
		form = ArticleForm(request.POST, instance=article) 
        # instance가 없다면 새로 생성, 있으면 덮어씌운다.
        # instance는 수정대상이 되는 객체를 지정한다. article을 미리 할당한 이유이다.
		if form.is_valid():					# 유효성 검사에 통과하면,
			form.save()						# DB에 저장하고,
			return redirect('articles:detail', article.pk) # detail로 바로 연결
    else:									 
    	form = ArticleForm(instance=article) 
        # update 페이지에는 input값이 기존에 있던 데이터로 채워져 있어야 한다.(수정이 용이하도록)
        # 모델 폼의 속성으로 instance 값을 추가하면 인풋값에도 자동으로 기존 값들이 채워진다.
	context = {
		'form': form,
		'article': article,
	}
	return render(request, 'articles/update.html', context) 
    # 날라온 요청이 GET 방식이면 update.html을 출력하고, 
    # POST 방식으로 온 요청값이 유효성 검사에 통과하지 못한다면, 아무일도 일어나지 않고, 
    # 에러 메시지와 함께 다시 update.html을 출력한다.
~~~

