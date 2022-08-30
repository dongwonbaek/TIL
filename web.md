# WEB



### 웹사이트의 구성요소

**HTML : 구조**

**CSS : 표현**

**Javascript : 동작**



**웹사이트와 브라우저**

- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 웹 표준이 등장



**웹 표준**

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)



### HTML (Hyper Text Markup Language)

**Hyper Text란?**

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트



#### 기본 구조

- 모든 구성요소는 여는 태그(\<p>) 와 닫는 태그(\</p>) `p는 예시` 그리고 그 사이에 담기는 컨텐츠로 구성되어 있음

- 상위 구성요소를 구성하는 하위 구성요소를 둘 수 있음(요소 중첩)

- VScode 에서 html 파일을 생성하고 ! tab을 순서대로 누르면 자동으로 기본구조가 완성된다.

- **\<html>\</html>** : 문서의 최상위(root)  요소, 페이지 전체의 컨텐츠를 감싼다.

  - **\<head>\</head>** : 문서 메타데이터(데이터를 위한 데이터) 요소

    - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등

    - **일반적으로 브라우저에 나타나지 않는 내용**

    - **\<title>*브라우저제목*\</title>** 

      - 브라우저 상단 타이틀

    - **\<meta charset="utf-8">** 

      - 문서 레벨 메타데이터 요소
      - 닫는 태그 X(빈요소)

    - **\<link href="*style.css*" rel="*stylesheet*">**

      - 외부 리소스 연결 요소
      - 닫는 태그 X(빈요소)

    - **\<script src="*javascript.js*">\</script>**

      - 스크립트 요소(JavaScript 파일/코드)

    - **\<style>\</style>**

      - CSS 직접 작성

      - ~~~html
        <style>
            p{
             color: black;
            }
        </style>
        ~~~

      

  - **\<body>\</body>** : 문서 본문 요소

    - 실제 화면 구성과 관련된 내용
    - **\<img src="*image파일경로*" alt="*대체텍스트*">**  
      - 파일경로에 있는 이미지를 삽입
      - 닫는 태그 X(빈요소)
      - **대체텍스트는 파일경로에 있는 이미지가 잘못되었을 경우 출력되는 텍스트이지만, 시각장애인이나, 기타 다른 장애를 가지고 있는 사람들이 웹페이지를 확인할 때 출력되는 음성서비스가 대체텍스트를 기반으로 하기 때문에 반드시 표현하려고 했던 이미지에 대한 설명으로 작성하여야 한다.**

  

#### 텍스트 요소

- 인라인 요소와 블록 요소로 나뉨
- 인라인 요소는 글자처럼 취급
- 블록 요소는 한 줄 모두 사용

- **제목요소**
  - 마크다운 문서와 같이, 1에서 6수준까지 있으며, 1이 가장 큰 제목이다.
  - 표현은 **\<h1>*제목\</h1>***
  - 단순히 글자크기를 목적으로 사용하면 안되고 제목수준을 목적으로 사용해야 한다.
- **문단**
  - **\<p>*문자\</p>*** 로 표현
  - 일반적인 문자 내용을 나타낼 때 많이 사용한다.
  - **\<br>** : 줄바꿈
  - **\<hr> **: 수평선
  - **\<b>*문자*\</b>** : 굵은 글씨 요소
  - **\<strong>*문자*\</strong>** : 굵은 글씨로 표현되고, 강조하고자 하는 요소로 지정됨.
  - **\<i>*문자*\</i>** : 기울임 글씨 요소
  - **\<em>*문자*\</em>** : 기울인 글씨로 표현되고, 강조하고자 하는 요소로 지정됨.
  - **\<pre>*문자*\</pre>** : HTML에 작성한 내용을 그대로 표현. 고정폭 글꼴이 사용되고 줄바꿈, 띄어쓰기 모두 적용됨.
  - **\<blockquote>*문자*\</blockquote>** : 텍스트가 긴 인용문, 들여쓰기를 한 것으로 표현됨
  - **\&lt;** 는 ''<''   **\&gt;** 는 ''>''
- **목록**
  - 순서가 없는 목록 \<ul>  (unordered list)
  - 순서가 있는 목록 \<ol>  (ordered list)

~~~html
<ul>
    <li>목록1</li>
    <li>목록2</li>
    <li>목록3</li>
</ul>
~~~

- **연결**
  - **\<a href="*https://링크*">*문자*\</a>**
  - [문자](https://링크) <--이런식으로 생성된다.



### CSS (Cascading Style Sheet)

- 스타일을 지정하기 위한 언어. 선택하고, 스타일을 지정한다.

- 위에서 아래로 흐르면서 스타일을 입혀준다.

- **id(#), class(.), 태그 순으로 스타일의 우선순위가 정해진다.**

- 같은 레벨이라면 나중에 '선언'된 것이 적용된다.

- 다만, 일반적으로 CSS 스타일링은 클래스로만 진행한다.

  - id 선택자는 일반적으로 하나의 문서에 1번만 사용하는 것이 관례이다.

  - id는 잘 활용하지 않고, 자바스크립트로 개발할 때 보통 활용한다.
  - 클래스 선택자는 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택



### css 기본 스타일

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀'기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을  받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
- 크기 단위(viewport)
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - ex) vw, vh, vmin, vmax

- 색상 키워드(background-color: red;)
  - 대소문자를 구분하지 않음
  - red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상(background-color: rgb(0, 255, 0);)
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
  - RGBA의 마지막 A는 투명도를 의미한다.
- HSL 색상(background-color: hsl(0, 100%, 50%);)
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식



### CSS Selectors

#### 선택자 정리

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - \# 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



#### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
  - 속성(property) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속 되는 것 예시
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것 예시
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등



### css 원칙 1

**모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.(좌측 상단에 배치)**



#### Box model

- 모든 HTML 요소는 box 형태로 되어있음

- 하나의 박스는 네 부분(영역)으로 이루어짐
  - **margin**: 테두리 바깥의 외부 여백, 배경색을 지정할 수 없음

  ~~~html
  .margin-1{
  	margin: 10px; <!--상하좌우 전부 10픽셀-->
  }
  
  .margin-2{
  	margin: 10px 20px; <!--상하 10픽셀, 좌우 20픽셀-->
  }
  
  .margin-3{
  	margin: 10px 20px 30px; <!--상 10픽셀, 좌우 20픽셀, 하 30픽셀-->
  }
  
  .margin-4{
  	margin: 10px 20px 30px 40px; <!-- 상 10픽셀, 우 20픽셀, 하 30픽셀, 좌 40픽셀, (시계방향으로 적용됨)-->
  }
  ~~~

  

  - **border**: 테두리 영역

  ~~~html
  .border{
  	border-width: 2px;
  	border-style: dashed;
  	border-color: black;
  } <!-- margin 과 마찬가지로 상하좌우로 나눠서 적용할 수 있다.-->
  
  .border{
  	border: 2px dashed black; <!-- 간단하게 표현도 가능하다.-->
  }
  ~~~

  

  - padding: 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용 
  - content: 글이나 이미지 등 요소의 실제 내용

![image-20220830164737280](web.assets/image-20220830164737280.png)

#### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box

  - Padding을 제외한 순수 contecnts 영역만을 box로 지정

- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함

  그럴 경우 box-sizing을 border-box로 설정

  ~~~html
  <style>
      .box{
          width: 100px;
          margin: 10px auto;
          padding: 20px;
          border: 1px solid black;
          color: white;
          text-align: center;
          background-color: blue;
      }
      
      .box-sizing{
          box-sizing: border-box;
          margin-top:50px;
      } 
  </style>
  <!-- 박스 사이즈를 테두리까지 설정하여 박스가 겹치는 일을 방지한다.-->
  
  <!--활용예시-->
  <body>
      <div class="box box-sizing">
          content-box
      </div>
  </body>
  ~~~

  

### CSS 원칙 2

- **모든 요소는 네보(박스모델)이고, 좌측상단에 배치.**
- **display에 따라 크기와 배치가 달라진다.**



### CSS Display



- **display: block**
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
  - 대표적인 블록 레벨 요소 **div**,  **ul**,  **ol**,  **li** ,  **p** ,  **hr** ,  **form**



- **display: inline**
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.
  - 대표적인 인라인 레벨 요소 **span,  a,  img,  input,  label,  b,  em,  i,  strong**



- **display: inline-block**
  - block 과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음



- **display: none**
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.



~~~html
<!--좌측 정렬-->
.box{
	margin-right: auto;
	text-align: left;
}

<!--중앙 정렬-->
.box{
	margin-left: auto;
	text-align: right;
}

<!--수평 정렬-->
.box{
	margin-right: auto;
	margin-left: auto;
	text-align: center;
}
~~~