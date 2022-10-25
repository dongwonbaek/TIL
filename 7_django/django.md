####  Framework 란?

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
        return render(request, 'hello.html', context)
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
      path('articles/', include('articles.urls')), # 모듈 : 앱이름.urls
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
      ** # fields = '__all__' 과 exclude 를 조합해서 사용하는 것이 보안상 안전하다고 한다.
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
    {% csrf_token %}	<!-- 유효성 검사(프론트 사이드) -->
    {{ form.as_p }}		<!-- context로 전달받은 객체를 어떤 방식(as_p)으로 출력할 것인지 표현 -->
    <input type="submit">
</form>
{% endblock content %}
~~~
`form 태그의 action 속성에 아무것도 넣지 않으면 자기 자신으로 보내게 됨`



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
        form = ArticleForm()		# ModelForm 양식을 건내주기 위해 할당
	context = {						# 유효성 검사에 통과하지 못했을 경우 여기로 점프하여 에러메시지가 담긴 form을 할당
        'form': form,
    }
    return render(request, 'articles/create.html', context)	# 에러메시지와 함께 create.html을 재출력
~~~



- Update (edit 기능과 합치기) :
  - 정확히는 views.py 의 update 함수와 edit 함수를 **form태그의 요청방식(GET or POST)**에 따라 다르게 작동하는 함수로 합치는 것

~~~python
# articles/views.py
from django.shortcuts import render, redirect
from article.models import Article
from .forms import ArticleForm 	# 유효성 검사를 위해 선언했던 ModelForm 참조

def update(request, pk):
	article = Article.objects.get(pk=pk) 	
    # Update(편집)는 instance에 사용할 객체를 미리 할당한다.
	if request.method == 'POST':			
    # 만약 날라온 요청이 POST 방식이라면, 날라온 데이터의 유효성을 검사한다.
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
		'form': form,		# form 태그 구성을 위해 인자로 넘기기
		'article': article,	# article의 pk를 넘기기 위해 넘기기
	}
	return render(request, 'articles/update.html', context) 
    # 날라온 요청이 GET 방식이면 update.html을 출력하고, 
    # POST 방식으로 온 요청값이 유효성 검사에 통과하지 못한다면, 아무일도 일어나지 않고, 
    # 에러 메시지와 함께 다시 update.html을 출력한다.
~~~



#### Admin site (Django 관리자 기능)

- Django 에는 관리자 페이지를 간단하게 작성할 수 있는 강력한 도구가 내장되어있음.
- 관리자 페이지는 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지임.
- models.py에 있는 class를 admin.py에 등록하는 방식으로 데이터베이스를 관리함.
- 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음.



##### Admin site 시작 순서

1. admin 계정 생성

   ~~~bash
   $ python manage.py createsuperuser
   # Username, Password는 필수, email은 선택사항
   # 비밀번호 생성시 보안상 터미널에 출력되지 않으나 실제로는 입력됨.
   ~~~

2. admin 에 모델 클래스 등록

   모델의 record를 모기 위해서는 admin.py 에 보고자 하는 class를 등록해야 함

   ~~~python
   # articles/admin.py
   from django.contrib import admin
   from .models import Article
   
   admin.site.register(Article) # 관리하고자하는 class를 import하여 다음과 같이 추가
   ~~~

3. http://localhost:8000/admin/ 으로 접속 후 로그인 (서버실행 후)



#### Static files (정적 파일 관리하기)

##### 정적파일이란?

- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일(요청에 따라 내용이 바뀌지 않음)

- 웹 서버는 일반적으로, 이미지, JS, CSS와 같은 준비된 정적파일을 제공할 수 있어야 함.

- Django에서는 settings.py 의 INSTALLED_APPS 에 django.contrib.staticfiles 이 기본적으로 존재하여 정적파일들을 관리할 수 있게 지원함.

- 앱의 하위 폴더에 static 폴더를 생성하여 관리할 수 있음

- templates 폴더와 마찬가지로 여러 앱의 static 폴더들은 모두 모아져 관리됨. 

  그러므로 templates와 같이 static 폴더 내에도 앱별로 구분할 수 있게 폴더를 따로 구성하는 것이 좋음.

  경로 예시 ) `article/static/article/example.jpg`

- 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 설정

  ~~~html
  {% load static %}
  <img src="{% static 'my_app/example.jpg' %}" alt="My image">
  ~~~

  

#### Django ModelForm 에서 bootstrap 활용하기

Django ModelForm 은 유효성 검사를 위한 도구이지만, 주어진 form 양식을 활용해야 해서 딱딱한 디자인을 가지고 있음. 하지만 bootstrap form을 적용하면 좀 더 부드러운 양식으로 변경할 수 있음.

~~~html
<form action="" method="POST">
  {% csrf_token %}
  {{ article.as_p }}  	<!-- 인풋박스가 안이쁨 -->
  <input type="submit">
  <a href="{% url 'article:detail' article.pk %}">돌아가기</a>
</form>
~~~

##### bootstrap form으로 적용하기

1. 가상환경에서 django-bootstrap5 설치

   ~~~bash
   $ pip install django-bootstrap5
   ~~~

2. settings.py 의 INSTALLED_APPS 에 설치한 bootstrap 앱 등록

   ~~~python
   INSTALLED_APPS = [
       'article',
       'django_bootstrap5' 		# 부트스트랩 버전마다 앱 이름이 달라질 수 있음! 검색요망
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ~~~

3. 템플릿에서 bootstrap load하고 사용

   ~~~html
   {% extends 'base.html' %}
   {% block content %}
   {% load django_bootstrap5 %}		<!-- 모듈 호출 -->
   <div class="m-3">
     <form action="" method="POST">
       {% csrf_token %}
       {% bootstrap_form article %}	
   	<!-- boostrap_form 은 고정, article은 context로 넘겨받은 ModelForm 인자임 -->
   	{% bootstrap_button button_type="submit" content="OK" %}
   	{% bootstrap_button button_type="reset" content="Cancel" %}
   	<!-- form뿐만 아니라 버튼도 구현가능하지만 사실 기존방식으로 구현하는 것이 편하다. -->
     </form>
   </div>
   {% endblock %}
   ~~~



#### Request 관련 메서드

- request.resolver_match.url_name

  - request의 name 속성을 출력한다.

    ~~~python
    # urls.py
    path('<int:pk>/delete/', views.delete, name='delete')
    >>> request.resolver_match.url_name
    output = 'delete'
    # 템플릿 내에서 활용할 수 있다.
    ~~~





### Django Auth

#### 회원가입

1. **accounts 앱 생성 및 등록**

   ~~~bash
   $ python manage.py startapp accounts
   # settings.py 의 INSTALLED_APPS 에 accounts 추가
   ~~~
   
2. **accounts/urls.py 분리**

3. **accounts/models.py 에 다음 내용 추가**

   ~~~python 
   from django.contrib.auth.models import AbstractUser
   
   class User(AbstractUser):	
       pass
   # Django에서 이미 활용되고 있는 AbstractUser를 상속받아 새로운 User 객체를 생성
   # 상속받아서 새롭게 만드는 이유는 커스텀 User모델은 기본 User모델과 동일하게 작동하면서도 
   # 필요할 때 맞춤설정할 수 있기 때문임
   # 단, 이 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 마쳐야 함
   ~~~

4. **settings.py 에 다음 내용 추가**

   ~~~python
   AUTH_USER_MODEL = 'accounts.User'
   # accounts앱의 User객체가 사용자관리에 사용될 기본 모델이라는 뜻
   # 이 내용은 무조건 첫 마이그레이션 전에 작성되어야 한다. (보안적인 이슈가 있을 수 있기 때문이다.)
   ~~~
   
5. **accounts/admin.py 에 커스텀 User 모델을 등록**

   ~~~python
   from django.contrib import admin
   from django.contrib.auth.admin import UserAdmin
   from django.contrib.auth import get_user_model
   
   admin.site.register(get_user_model(), UserAdmin)
   # get_user_model() 함수는 현재 활성화된 모델, 즉 위의 4번에서 진행된 AUTH_USER_MODEL 의 값을 가져온다. 반드시 from django.contrib.auth import get_user_model 로 참조해야 한다.
   ~~~

6. **accounts/forms.py 생성**

   ~~~python
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib.auth import get_user_model
   
   class CustomUserCreationForm(UserCreationForm):
   # 사용자생성을 위해 Django에서는 기본적으로 UserCreationForm이라는 입력 Form을 지원한다. 
   # (UserCreationForm은 ModelForm을 상속 받아서 만들고 있음)
   # 하지만 UserCreationForm은 기본지원대상이 User객체이지만 
   # 우리가 사용하는 User객체는 3번의 내용에서 정의했듯이 새롭게 커스텀된 User객체이기 때문에 사용할 수 없다. 
   # 그러므로 User객체를 커스텀한 것과 같이 UserCreationForm 또한 새롭게 커스텀하여 사용해야 한다.
       class Meta:
        model = get_user_model() 
           # settings.py 에서 AUTH_USER_MODEL로 정의한 커스텀된 User객체가 들어온다.
           fields = ['username', 'email']
   ~~~
   
7. **accounts/templates/accounts/signup.html 생성 및 작성**

8. **accounts/views.py 작성**

   ~~~python
   from django.shortcuts import render, redirect
   from .forms import CustomUserCreationForm
   from .models import User
   
   def signup(request):
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('accounts:index')
       else:
           form = CustomUserCreationForm()
       context = {
           'form':form,
       }
       return render(request, 'accounts/signup.html', context)
   # 게시판 작성과 거의 유사하다.
   ~~~

   `변경 가능한 것은 변수화하는 것이 좋다.`

#### **기본 User 객체에서 정의된 메서드**

- create_user() : 암호화된 유저 생성

  ~~~python
  User.objects.create_user('아이디', '이메일', '비밀번호')
  # SHA-256 방식의 비밀번호 암호화를 통해 회원정보를 생성하여 User DB에 저장한다는 메서드이다.
  # 반환값은 생성된 유저객체이다.
  ~~~

  `SHA-256 암호화 방식은 단방향 해시함수를 활용한 암호화 방식으로 우리가 입력한 비밀번호를 단방향 해시함수에 입력값으로 넣어 다이제스트로 암호화하며 이 때 출력된 값을 가지고 입력값을 추출하는 복호화가 불가능함.`

  ` 하지만 단방향 해시함수의 경우 레인보우 공격과 무차별 대입 공격 등으로 문제가 발생할 수 있는데, 이를 보완하기 위해서 솔팅(salting) 방식과 키 스트레칭(Key Stretching) 방식을 추가적으로 활용함`

  `솔팅(Salting) : 패스워드에 임의의 문자열은 추가하여 해시함수에 입력`

  `키 스트레칭(Key Stretching) : 해시함수에 대입 후 출력값을 또 다시 해시함수에 넣는 과정을 반복 `

  

- set_password() : 비밀번호 변경

  ~~~python
  user = User.objects.get(pk=2)
  user.set_password('new password')
  user.save()
  ~~~

  

- authenticate() : 인증

  ~~~python
  from django.contrib.auth import authenticate
  user = authenticate(username='john', password='secret')
  # 비밀번호가 틀리면 유저 객체를 반환하지 않는다.
  ~~~

  

#### 로그인 로직

쿠키 = 장바구니

- URL : GET / accounts/ login /
  - 처리 : 사용자에게 From을 제공한다.
- URL : POST / accounts / login /
  - 처리 : 로그인 로직처리 
    - 사용자인지 확인하고, django_session 테이블에 저장, 쿠키 주기
  - (성공) 게시글 목록 페이지로 redirect
  - (실패) 로그인 Form





#### 회원가입 및 로그인 views.py 구성

~~~python
# accounts/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth import login as auth_login 	# login 이름이 겹치기 때문에 바꿔줌
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()					# save()의 리턴값은 해당 모델의 인스턴스이다.
            auth_login(request, user)			# 유효한 요청이 들어왔으면 요청대로 저장하고 가입된 정보로 바로 로그인한다.
            return redirect('accounts:index')	
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    # AuthenticationForm 는 ModelForm이 아니라 일반 Form을 상속받는다. 그래서 위의 양식이 조금 달라짐.
    if form.is_valid(): 	# ModelForm이나 일반 Form이나 is_valid()로 유효성 검증이 가능하다.
        auth_login(request, form.get_user())	# 세션에 저장 (로그인)
        return redirect(request.GET.get('next') or 'accounts:index') 
    	# 파이썬의 단축평가 : redirect(A or B) 일 때 A가 참이면 A를 선택, A가 거짓이고 B가 참이면 B를 선택한다.
        # A가 참일 경우 B의 참거짓 여부는 고려하지 않고 A를 선택하게 된다.
        # @login_required가 붙은 함수들에 의해서 login함수에 도달했다면, 
        # 그 위치를 기억했다가 로그인이 완료되고나서 다시 그 위치로 보내주는 역할을 한다.
    else:
        form = AuthenticationForm()
	context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)
~~~



#### 로그인 여부에 따른 템플릿 분기

~~~html
<!-- templates/base.html -->
{% if request.user.is_authenticated %}	
<!-- is_authenticated 는 request의 속성들 중 하나이고 로그인여부에 따라 True나 False값을 가지게 된다. -->
	<p>{{ request.user }}님 환영합니다!</p>
<!-- {{ request.user }}는 따로 설정없이도 현재 로그인된 username을 출력한다. -->
{% endif %}
{% if request.user.is_authenticated %}
    <a href="{% url 'accounts:index' %}">회원목록</a>
    <a href="{% url 'accounts:logout' %}">로그아웃</a>
{% else %}
    <a href="{% url 'accounts:signup' %}">회원가입</a>
    <a href="{% url 'accounts:login' %}">로그인</a>
{% endif %}
~~~



#### 로그인 여부에 따른 접근 제한 설정

~~~python
# articles/views.py
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required	# login_required는 decorators에서 가져온다.

@login_required	 	# @login_required가 붙어있는 함수에 로그인을 하지않고 접근하게 되면 로그인 창으로 보내지게 된다.
def create(request):
    if request.method == "POST":
        article = ArticleForm(request.POST)
        if article.is_valid:
            article.save()
            return redirect("article:index")
    else:
        article = ArticleForm()
    context = {
        "article": article,
    }
    return render(request, "article/create.html", context)
~~~

#### `어떻게 login_required 함수는 별도의 경로설정없이 로그인 창으로 보낼 수 있는 것일까?`

`django의 공식문서를 살펴보면, login_required가 적용된 함수에 로그인되지 않은 상태로 접근했을 때, settings.LOGIN_URL로 redirect된다고 나와 있다.`

`이 때 LOGIN_URL은 별도의 설정이 없다면 기본값이 '/accounts/login/' 인 것을 확인할 수 있다. `

`즉, accounts와 login 이름은 관용적이기도 하면서 동시에 기본값들로 설정이 되어 있기 때문에 변경하지 않는 것이 좋다.`	

`이는 login함수를 auth_login으로 변경하여 사용하는 이유이기도 하다.`

#### 로그아웃

~~~python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
~~~



#### 회원정보 수정

~~~python
from .forms import CustomUserChangeForm	# 사전에 forms.py 에서 UserChangeForm을 상속하는 CustomUserChangeForm을 정의해야한다.

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user) 
        # Articles의 update.html 과 같이 instance를 인자로 받는다. instance에는 request.user (요청한 유저의 정보)가 담긴다.
        if form.is_valid():
            form.save()
            return redirect('accounts:detail')
	else:
        form = CustomUserChangeForm(instance=request.user)
	context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)
~~~



#### 비밀번호 변경

~~~python
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST) # 요청한 유저의 정보와 요청된 정보(변경된 비밀번호)를 인자로 받는다.
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) 
            # 암호가 변경되면 기존세션과 회원인증정보가 일치하지 않아 로그인 상태가 유지되지 못하므로 재로그인해야함.
            # 암호를 변경해도 세션을 동일하게 가져가기 위해선 위의 함수를 import해서 사용해야함. 
            # 요청과 새로운 비밀번호가 적용된 유저정보를 인자로 받음
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html', context)
~~~



#### 회원탈퇴

~~~python
from django.contrib.auth import logout as auth_logout
def delete(request):
    request.user.delete()	# 요청한 유저 객체를 삭제하는 명령어, delete() 는 삭제와 동시에 저장된다.
    auth_logout(request)	# 삭제 후 로그아웃해야 세션에 삭제된 유저 객체가 남지 않게된다. 삭제명령어와 순서를 꼭 지켜야 한다.
    return redirect('accounts:login')
~~~



~~~python
CustomUserCreationForm(request.POST)
CustomUserChangeForm(request.POST, instance=request.user)
PasswordChangeForm(request.user, request.POST)
AuthenticationForm(request, data=request.POST)
auth_login(request, form.get_user)
update_session_auth_hash(request, form.user)
~~~



#### Image 업로드(사용자)

1. pillow, django-imagekit 모듈 설치

   ~~~bash
   $ pip install pillow			# 파이썬을 활용해 이미지를 업로드하기 위한 모듈
   $ pip install django-imagekit	# 이미지의 용량, 사이즈를 조절하여 저장하는 모듈
   ~~~

2. settings.py 추가

   ~~~python
   # config/settings.py
   # pillow 는 추가할 필요없다.
   INSTALLED_APP = [
       'imagekit',
       ...
   ]
   MEDIA_ROOT = BASE_DIR / 'media' 	# 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로 (DB에 이미지를 직접 저장하지 않음)
   MEDIA_URL = '/media/'				# 업로드 된 파일의 주소(URL)를 만들어 주는 역할
   ~~~

3. urls.py 추가

   ~~~python
   # config/urls.py
   from django.conf.urls.static import static
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
   # 사용자가 업로드 한 파일이 우리 프로젝트에 업로드 되지만, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함
   # 업로드 된 파일의 URL == settings.MEDIA_URL
   # 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
   ~~~

4. models.py 설정

   ~~~python
   # articles/models.py
   from imagekit.models import ProcessedImageField
   from imagekit.processors import ResizeToFill # ResizeToFit
   class Article(models.Model):
       title = models.CharField(max_length=20)
       content = models.TextField()
       image = ProcessedImageField(
           blank=True, upload_to='images/', 	
           # 이미지가 꼭 필요하진 않으므로 blank=True, 사용자에게 받은 이미지가 저장될 경로를 upload_to로 설정
           processors=[ResizeToFill(400, 300)], 
           # 이미지 사이즈를 결정, fill은 사이즈에 맞춰 이미지를 자르고, fit은 사이즈에 이미지를 변형하여 넣음
           format='JPEG', # 저장형식 설정
           options={'quality':80}) # 이미지의 품질을 설정하여 용량을 조절할 수 있음
       	# 작성 후 마이그레이션 진행
   ~~~

5. HTML 설정

   ~~~html
   <form action="" method="POST" enctype="multipart/form-data"> 
       <!-- enctype은 파일, 이미지에 대한 인코딩 속성으로, 파일 업로드에 반드시 필요 -->
       {% csrf_token %}
       {{ bootstrap_form form }}
       <input type="submit">
   </form>
   ~~~

6. views.py 설정

   ~~~python
   # articles/views.py
   def create(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES) # 업로드한 파일은 request.FILES 객체로 전달됨
           ...
   ~~~

7. 템플릿에서 img 태그 활용

   ~~~html
   <img src="{{ article.image.url }}" alt="{{ article.image }}"> <!-- article은 context로 넘겨받은 변수로, 바뀔 수 있음 -->
   <!-- article.image.url == 업로드 파일의 경로 -->
   <!-- article.image == 업로드 파일의 파일 이름 -->
   ~~~



#### Django Messages

1. settings.py 설정

   ~~~python
   MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
   ~~~

2. views.py 설정

   ~~~python
   # artilces/views.py
   from django.contrib import messages # messages를 import
   
   def create(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES)
           if form.is_valid():
               form.save()
               messages.success(request, '글 작성이 성공적으로 완료되었습니다.')
               return redirect('articles:index')
       else:
           form = ArticleForm()
       context = {
           'form': form,
       }
       return render(request, 'articles/create.html', context)
   ~~~

3. HTML 설정

   ~~~html
   <!-- base.html -->
   	{% if messages %} <!-- messages가 존재한다면 실행 -->
         {% for message in messages %} <!-- 반드시 for문을 활용해야 함 -->
           <div class="alert alert-{{ message.tags }}"> <!-- message.tags 에는 views에서 정의했던 success가 담겨있음 -->
             {{ message }}	<!-- message 에는 views에서 정의한 텍스트가 담겨있음 -->
           </div>
         {% endfor %}
       {% endif %}
   ~~~

   

#### 댓글 기능 구현

- ##### **댓글 생성**

    1. 댓글(comment) 모델 선언

       ~~~python
       # articles/models.py

       class Comment(models.Model):
           content = models.CharField(max_length=100)
           created_at = models.DateTimeField(auto_now_add=True)
           article = models.ForeignKey(Article, on_delete=models.CASCADE)
           # ForeignKey 필드는 다른 모델의 객체를 가져온다.
           # 이 때 on_delete 속성은 참조하는 객체가 삭제되었을 때 같이 삭제하는지에 대한 설정이다. CASCADE는 같이 삭제한다.
           # 작성 후 마이그레이션 진행
           # 실제로 생성되는 DB에는 article이 아니라 article_id가 생성되지만 comment객체의 article을 검색하면 참조되는 article객체가 출력된다.
           # 물론 article_id로 article객체의 id값만 출력할 수도 있다.(article.id 도 가능하다.)	
       ~~~

    2. 사용자로부터 댓글 데이터를 입력받기 위한 CommentForm 작성

       ~~~python
       # articles/forms.py
       from .models import Article, Comment
       class CommentForm(forms.ModelForm):
           class Meta:
               model = Comment
               fields = ['content'] # 내용만 입력받을 것이기 때문에
       ~~~

    3. detail 페이지에서 CommentForm 출력

       ~~~python
       # articles/views.py
       from .forms import ArticleForm, CommentForm
       def detail(request, pk):
           article = Article.objects.get(pk=pk)
           comment_form = CommentForm()
        	context = {
               'article': article,				# 게시글 구성을 위한 게시글 객체 전달
               'comment_form': comment_form,	# 댓글작성을 위한 폼 전달
           }
           return render(request, 'articles/detail.html', context)
       ~~~

    4. detail 템플릿에서 CommentForm 출력

       ~~~html
       {% block content %}
       ...
       <form action="{% url 'articles:comments_create' article.pk %}", method='POST'>
           {% csrf_token %}
           {{ bootstrap_form comment_form }}
           <input type="submit">
       </form>
       {% endblock %}
       ~~~

    5. urls.py 에서 댓글 작성을 위한 새로운 url 생성
    
       ~~~python
       # articles/urls.py
       urlpatterns = [
           ...,
           path('<int:pk>/comments/', views.comments_create, name='comments_create'),
       ]
       ~~~
    
    6. views.py 에서 comments_create 함수 작성
    
       ~~~python
       # articles/views.py
       def comments_create(request, pk):
           article = Article.objects.get(pk=pk)
           comment_form = CommentForm(request.POST)
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)	
               # save 메서드의 commit속성을 활용하여 ((commit=False)는 저장되지않지만 save의 리턴값을 사용할 수 있게 된다.)
               comment.article = article
               # 저장 전에 비어있는 comment객체의 article에 위에서 정의했던 article객체를 넣어주고,
               comment.save()
               # 완전히 저장한다.
               # Comment모델은 Article객체를 외래키로 참조하고 있지만, 댓글을 작성한다고 알아서 참조되는 것이 아니기 때문에 위의 과정이 필요함.
       	return redirect('articles:detail', article.pk)
       ~~~
    
    7. views.py 에서 context에 댓글목록 전달
    
       ~~~python
       # articles/views.py
       from .forms import ArticleForm, CommentForm
       def detail(request, pk):
           article = Article.objects.get(pk=pk)
           comment_form = CommentForm()
        	context = {
               'article': article,
               'comment_form': comment_form,
               'comments': article.comment_set.all(),	
               # article.comment_set.all()은 article객체를 가지고 있는 comment객체들의 집합을 불러오는 역참조 API 이다.
               # 역참조를 사용하지 않는다면, Comment.objects.filter(article=article) 가 된다.
               'comments_counts': article.comment_set.count(),
               # count() API를 활용하여 댓글을 개수를 넘겨줄 수도 있다.
           }
           return render(request, 'articles/detail.html', context)
       ~~~
    
    8. detail 템플릿에서 댓글 목록 출력
    
       ~~~html
       {% block content %}
       <p>
           {{ comments_counts }}개의 댓글
       </p>
       {% for comment in comments %}
       <p>
           {{ comment.content }}
       </p>
       {% endfor %}
       {% endblock %}
       ~~~
    
- ##### **댓글 삭제**

    1. urls.py

       ~~~python
       # articles/urls.py
       urlpatterns = [
           ...,
           path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
           # 2개의 pk를 각각 다른 변수명으로 받는다.
       ]
       ~~~

    2. views.py

       ~~~python
       # articles/views.py
       def comments_delete(request, article_pk, comment_pk): 
           # article_pk로 리턴값을 통해 돌아갈 detail페이지를 결정하고, comment_pk로 삭제할 comment를 결정한다.
           if request.method == POST:
               comment = Comment.objects.get(pk=comment_pk)
               comment.delete()
           return redirect('articles:detail' article_pk)
       ~~~

    3. templates

       ~~~html
       <!-- detail.html -->
       {% block content %}
       {% for comment in comments %}
       <p>
           {{ comment.content }} 
           <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
               <!-- comments_delete함수에서 활용할 2개의 pk값을 같이 담아서 보내줘야한다. 순서도 꼭 지켜야한다. -->
               {% csrf_token %}
               <input type="submit" value="삭제">
       	</form>
       </p>
       {% endfor %}
       {% endblock %}
       ~~~




### 좋아요(LIKE) 기능 (M : N)

1. 모델 정의

   ~~~python
   # articles/models.py
   class Article(models.Model):
       ...
   	like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
       # 괄호의 첫번째 인자는 M:N 관계를 가질 모델을 넣고, 두번째는 related_name='역참조에사용할 이름' 으로, 첫번째 인자로 넣은 모델을 이미 외래키로 참조하고 있다면, 역참조(..._set)할 때 어떤 객체를 참조할 것인지 알 수 없기 때문에, 역참조에 사용할 이름을 따로 명시한다. 이는 ForeignKey에도 명시하여 사용할 수 있다. 단, related_name을 명시하면, _set 은 사용할 수 없다.
   ~~~

2. url 추가

   ~~~python
   # articles/urls.py
   urlpatterns = [
       ...,
       path('<int:pk>/like/', views.like, name='like'),
   ]
   ~~~

3. view 함수 추가

   ~~~python
   # articles/views.py
   
   def like(request, pk):
       review = Review.objects.get(pk=pk)
       # if request.user not in review.like_users.all():
       # 위 방법도 가능하지만, 밑의 방법이 더 시간을 단축시킬 수 있다.
       if review.like_users.filter(id=request.user.id).exists():
       # review객체의 like_users객체들에서 id가 요청을 보낸 User객체의 id가 있으면 True, 없으면 False
   		review.like_users.remove(request.user)
           # 있으면, 로그인한 유저객체를 삭제한다.
       else:
           review.like_users.add(request.user)
           # 없으면, 로그인한 유저객체를 추가한다.
       return redirect('reviews:detail', pk)
   ~~~

   

### Follow 기능

1. url 추가

   ~~~python
   # accounts/urls.py
   urlpatterns = [
   	...,
       path('<int:pk>/', views.detail, name='detail'),
       path('<int:pk>/follow/', views.follow, name='follow'),
   ]
   ~~~

2. views 함수 추가

   ~~~python
   # accounts/views.py
   def detail(request, pk):
       context = {
           'user': get_user_model().objects.get(pk=pk)
       }
       return render(request, 'accounts/detail.html', context)
   # 팔로우를 할 수 있는 팔로우 버튼이 개개인의 프로필페이지에 있어야 자연스러움.(detail필요)
   
   def follow(request, pk):
       user = get_user_model().objects.get(pk=pk)
       # 팔로우할 유저객체를 가져옴
       if request.user != user:
   	# 팔로우할 대상이 자기자신이 되면 안되니, 조건문 작성
           if request.user.followings.filter(id=user.pk).exists():
           # 요청보낸 유저가 이미 유저객체를 팔로우했을 경우,
               request.user.followings.remove(user)
               # 유저객체를 제거함으로써 언팔로우
           else:
   		# 팔로우하지 않았을 경우,
               request.user.followings.add(user)
               # 유저객체를 추가함으로써 팔로우
       return redirect('accounts:detail', pk)
   	# 함수가 종료되면 무조건 유저객체 프로필페이지로 이동
   ~~~

3. Template 수정

   ~~~html
   <!-- accounts/detail.html -->
   {% block content %}
     <h1>{{ user.username }}
       님의 정보</h1>
     {% if request.user != user %}
     <!-- 자기 자신의 프로필페이지일 때는 팔로우버튼이 보이면 안됨 -->
   	<a href="{% url 'accounts:follow' user.pk %}">
         {% if user in request.user.followings.all %}
           팔로우 취소
         {% else %}
           팔로우
         {% endif %}
   	</a>
     {% endif %}
   {% endblock content %}
   ~~~

   





#### github-flow 규칙

1. 깃헙의 콜라보레이터에서 협업자들을 추가한다. 협업자들은 함께 작업할 저장소를 클론하여 로컬로 옮긴다.

2. master(main) 브랜치에서 새로운 브랜치(토픽, topic)를 만들고 변경. - 상세하게 작성한다. git branch accounts, master에서는 절대 개발해선 안된다. 브랜치만들고 거기서 개발해야함 

   git switch master -> master브랜치로 이동

   git checkout master -> master브랜치로 이동

   git checkout -b accounts/update -> **accounts/update 브랜치를 만들고 이동**



Django 파이썬 패키지

- django==3.2.13
- black
- django-bootstrap5
- django-imagekit
- pillow
- django-extensions
- ipython



view함수는 http response 객체를 응답한다. 템플릿을 응답하는 것이 아니다.

render : 2xx + html

redirect : 3xx

login_required : 3xx

url을 잘못 적었을 때 (클라이언트 잘못) : 4xx

url에러를 제외한 모든 에러 (서버 잘못) : 5xx



get_object_or_404(모델, pk=pk) 는 모델.objects.get(pk=pk) 와 같은 방식으로 동작하지만, 존재하지 않는 pk로 접근시에 5xx 에러가 아닌 4xx 에러를 띄워준다.

from django.views.decorators.http import require_POST, require_safe, require_GET

require_POST를 사용하게 되면, login_required 의 next 파라미터는 동작하지 않게 된다.