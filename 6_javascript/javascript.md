# Javascript



#### JavaScript의 필요성

- 브라우저 화면을 '동적'으로 만들기 위함
- 브라우저를 조작할 수 있는 유일한 언어



#### DOM(Document Object Model)

-  HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - window : DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략)
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며, \<body> 등과 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen
- 파싱 (Parsing)
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정



#### BOM (Browser Object Model)

- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭



#### DOM 조작

1. 선택 (Select)

   ~~~javascript
   document.querySelector(selector)
   // 제공한 선택자와 일치하는 element 하나를 선택
   // 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)
   
   document.querySelectorAll(selector)
   // 제공한 선택자와 일치하는 여러 element들을 선택
   // 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
   // 지정된 셀렉터에 일치하는 NodeList를 반환
   ~~~

   `이 외에도 다양한 선택관련 메서드들이 존재하지만 위 두 가지를 사용하는 것이 구체적이고 유연하게 선택자를 선택할 수 있음. `

   

2. 변경 (Manipulation)

   ~~~javascript
   document.createElement()
   // 작성한 태그 명의 HTML 요소를 생성하여 반환
   
   Element.append()
   // 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
   // 여러 개의 Node 객체, DOMString을 추가할 수 있음
   // 반환 값이 없음
   
   Node.appendChild()
   // 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입(Node만 추가 가능)
   // 한번에 오직 하나의Node만 추가할 수 있음
   // 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
   
   Node.innerText
   // Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)(사람이 읽을 수 있는 요소만 남김)
   // 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
   ~~~

3.  삭제

   ~~~javascript
   ChildNode.remove()
   // Node가 속한 트리에서 해당 Node를 제거
   
   Node.removeChild()
   // DOM에서 자식 Node를 제거하고 제거된 Node를 반환
   // Node는 인자로 들어가는 자식 Node의 부모 Node
   ~~~

4. 속성 관련 메서드

   ~~~javascript
   Element.setAttribute(name, value)
   // 지정된 요소의 값을 설정
   // 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
   
   Element.getAttribute(attributeName)
   // 해당 요소의 지정된 값(문자열)을 반환
   // 인자(attributeName)는 값을 얻고자 하는 속성의 이름
   ~~~

   

스크립트를 배치하는 고전적인 방법은 스크립트 요소를 본문의 맨 마지막(\<\\body> 태그 바로 앞)에 배치하는 것이다.



최신 기법은 defer 특성을 활용하여 브라우저가 \<script> 태그를 마주쳐도 그 이후의 HTML 콘텐츠를 계속 불러오도록 지정한다. 단, 외부에서 스크립트를 불러올 때만 사용가능하다.

~~~javascript
<script src="script.js" defer></script>
~~~



객체 내에서는 메서드로 arrow function을 사용할 수 없다.



#### 변수

- let 변수명
  - 재할당 가능, 재선언 불가능
- const 변수명
  - 재할당 불가능, 재선언 불가능
- var 변수명
  - 재할당 가능, 재선언 가능
  - 호이스팅 되는 특성으로 예기치 못한 문제가 생길 수 있으므로 const, let을 사용하는 것을 권장
  - 호이스팅 : 변수를 선언 이전에 참조할 수 있는 현상, 변수 선언 이전의 위치에서 접근 시 undefined를 반환



#### 데이터 타입

- 원시 타입 (Primitive type)
  - 객체 (object) 가 아닌 기본 타입
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사됨
- 참조 타입 (Reference type)
  - 객체 (object) 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨



- 숫자 타입 (Number)
  - 정수, 실수 구분 없는 하나의 숫자 타입
  - 부동소수점 형식을 따름
  - NaN (Not-A-Number) : 산술연산이 불가능할 때 반환되는 값
- 문자열 (String) 타입
  - 텍스트 데이터를 나타내는 타입
  - 16비트 유니코드 문자의 집합
  - 작은 따옴표 또는 큰따옴표 모두 가능
  - 템플릿 리터럴 (Template Literal)
    - 따옴표 대신 backstick(``) 으로 표현
    - &{변수명} 형태로 변수를 문자열 안에 삽입 가능
- undefined
  - 변수의 값이 없음을 나타내는 데이터 타입
  - 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined 가 할당됨
- null
  - 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
- Boolean 타입
  - 논리적 참 또는 거짓을 나타내는 타입
  - true 또는 false로 표현
  - 조건문 또는 반복문에서 유용하게 사용
    - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 현변환 규칙에 따라 true 또는 false로 변환됨

| 데이터 타입 |    거짓    |        참        |
| :---------: | :--------: | :--------------: |
|  Undefined  | 항상 거짓  |        X         |
|    Null     | 항상 거짓  |        X         |
|   Number    | 0, -0, NaN | 나머지 모든 경우 |
|   String    | 빈 문자열  | 나머지 모든 경우 |
|   Object    |     X      |     항상 참      |



#### 연산자

- 할당 연산자

  - 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
  - 다양한 연산에 대한 단축 연산자 지원
  - 파이썬과 대부분 비슷하지만, 1씩 증가시키는 연산자 '++', 1씩 감소시키는 연산자 '--' 등추가된 연산자들이 존재

- 비교 연산자

  - 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
  - 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
    - 알파벳끼리 비교할 경우 알파벳 순서상 후순위가 더 크고 소문자가 대문자보다 더 크다.

- 동등 비교 연산자 ( == )

  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  - 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  - 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음

- 일치 비교 연산자 ( === )

  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  - 엄격한 비교(파이썬의 ==와 같음)가 이루어지며 암묵적 타입 변환이 발생하지 않음(위의 표 참고)

- 논리 연산자

  - 세 가지 논리 연산자로 구성
    - and 연산은 '&&' 
    - or 연산은 '||'
    - not 연산은 '!'
  - 단축 평가 지원
    - false && true => false
    - true || false => true

- 삼항 연산자 (Ternary Operator)

  - 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자

  - 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용

  - 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

  - ~~~javascript
    console.log(true ? 1 : 2) // 1
    console.log(false ? 1 : 2) // 2
    ~~~

  

#### 조건문

- if , else if, else문

  - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
  - 조건은 소괄호() 안에 작성
  - 소괄호 안에 작성된 표현식이 true이면 실행할 코드를 중괄호{} 안에 작성
  - 이 때 블록 스코프가 생성됨

- switch 문

  - 조건 표현식의  결과값이 어느 값(case)에 해당하는지 판별

  - 주로 특정 변수의 값에 따라 조건을 분기할 때 활용

  - 조건이 많아질 경우 if문보다 가독성이 나음

  - 표현식(expression)의 결과값을 이용한 조건문

  - 표현식의 결과값과 case문의 오른쪽 값을 비교

  - break 및 default문은 선택적으로 사용 가능

  - break문이 없으면 모든 케이스를 전부 검사함

  - break문을 만나거나 default문을 실행할 때 까지 다음 조건문 실행

  - ~~~javascript
    switch(expression) {
        case 'first value': {
            // do something
            [break]
        }
        case 'second value': {
            // do something
            [break]
        }
    	[default: {
         	// do something
         }]
    }
    ~~~

  

#### 반복문

- while 문

  - 조건문이 참(true)인 동안 반복 시행

  - 조건은 소괄호 안에 작성, 실행할 코드는 중괄호 안에 작성

  - 블록 스코프 생성됨

  - ~~~javascript
    let i = 0
    while (i < 6) {
        console.log(i) // 0, 1, 2, 3, 4, 5
        i += 1
    }
    ~~~

- for 문

  - 세미콜론(;)으로 구분되는 세 부분으로 구성

  - initialization

    - 최초 반복문 진입 시 1회만 실행되는 부분

  - condition

    - 매 반복 시행 전 평가되는 부분

  - expression

    - 매 반복 시행 이후 평가되는 부분

  - 블록스코프 생성

  - ~~~javascript
    for (let i = 0; i < 6; i++) {
        console.log(i) // 0, 1, 2, 3, 4, 5
    }
    ~~~

- for ... in 문

  - 객체(object)의 속성들(key)들을 순회할 때 사용

  - 배열도 순회 가능하지만 권장하지 않음 (객체 순회에 적합)

  - 실행할 코드는 중괄호 안에 작성

  - 블록 스코프 생성

  - ~~~javascript
    const capitals = {
        korea: 'seoul',
        france: 'paris',
        USA: 'washington D.C.'
    }
    
    for (let capital in apitas) {
        console.log(capital) // korea, france, USA
    }
    ~~~

- for ... of 문

  - 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용 (배열 순회에 적합)

  - 실행할 코드는 중괄호 안에 작성

  - 블록 스코프 생성

  - ~~~javascript
    const fruits = ['딸기', '바나나', '메론']
    
    for (let fruit of fruits) {
        fruit = fruit + '!'
        console.log(fruit)
    }
    ~~~



#### 함수

- JavaScript에서 함수를 정의하는 방법은 2가지

  - 함수 선언식 (function declaration)

    - 함수의 이름과 함께 정의하는 방식

    - 함수의 이름, 매개변수, 함수 body(중괄호) 로 구성

    - ~~~javascript
      function add(num1, num2) {
          return num1 + num2
      }
      ~~~

  - 함수 표현식 (function expression)

    - 함수를 표현식 내에서 정의하는 방식

    - 함수의 이름을 생략하고 익명 함수로 정의 가능

    - 함수의 이름(생략 가능), 매개변수, 함수 body(중괄호) 로 구성

    - ~~~javascript
      const add = function (num1, num2) {
          return num1 + num2
      }
      add(1, 2) // 3
      ~~~

- JavaScript에서 함수는 일급 객체에 해당

  - 변수에 할당 가능
  - 함수의 매개변수로 전달 가능
  - 함수의 반환 값으로 사용 가능

- 매개변수 뒤 '=' 문자 뒤 기본 인자 선언 가능

  - ~~~javascript
    const greeting = function (name = 'Anonymous') {
        return `Hi ${name}`
    }
    greeting() // Hi Anonymous
    ~~~

- 매개변수와 인자의 개수가 불일치해도 결과값이 출력됨

  - 매개변수보다 인자의 개수가 많을 경우 매개변수만큼 출력

  - ~~~javascript
    const noArgs = function () {
    	return 0
    })
    no Args(1, 2, 3) // 0
    const twoArgs = function (arg1, arg2) {
        return [arg1, arg2]
    }
    twoArgs(1, 2, 3) // [1, 2]
    ~~~

  - 인자의 개수보다 매개변수가 많을 경우 입력되지 않은 인자는 undefined로 출력

  - ~~~javascript
    const threeArgs = function (arg1, arg2, arg3) {
        return [arg1, arg2, arg3]
    }
    threeArgs()		// [undefined, undefined, undefined]
    threeArgs(1) 	// [1, undefined, undefined]
    threeArgs(1,2)	// [1, 2, undefined]
    ~~~

- rest parameter(...) 를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음

  - ~~~javascript
    const restOpr = function (arg1, arg2, ...restArgs){
        return [arg1, arg2, restArgs]
    }
    restOpr(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    restOpr(1, 2) // [1, 2, []]
    ~~~

- spread operator(...)를 사용하면 배열 인자를 전개하여 전달 가능

  - ~~~javascript
    const spreadOpr = function (arg1, arg2, arg3) {
        return arg1 + arg2 + arg3
    }
    const numbers = [1, 2, 3]
    spreadOpr(...numbers) // 6
    ~~~

- 함수 - 호이스팅

  - 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 호이스팅 발생
  - 함수호출 이후에 선언해도 동작한다.
  - 반면에 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
  - 이는 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따른다는 것을 나타냄
  - 함수표현식을 var 키워드로 작성한 경우 변수가 선언 전에 undefined로 초기화 되어 다른 에러가 발생

- 화살표 함수 (Arrow Function)

  - 함수를 비교적 간결하게 정의할 수 있는 문법

  - function 키워드 생략 가능

  - 함수의 매개변수가 단 하나 뿐이라면, **소괄호도 생략 가능**

  - 함수 body가 표현식 하나라면 **중괄호와 return도 생략 가능**

  - ~~~javascript
    const arrow1 = function (name) {
        return `hello, ${name}`
    }
    // 위 함수 표현식을 화살표 함수로 표현하면 이렇게 된다.
    const arrow1 = name => `hello, ${name}`
    ~~~



#### 문자열 (String)

~~~javascript
문자열변수.include(value)
// 문자열변수에 value값이 있는지 확인하여 True or False 반환

문자열변수.split(value)
// value에 값을 넣지 않으면 기존 문자열을 배열에 담아서 반환
// value가 빈 문자열('') 일 경우 각 문자로 나눈 배열을 반환
// value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환

문자열변수.replace(from, to)
// 문자열변수에 from 값이 존재할 경우, 1개만 to 값으로 교체하여 반환

문자열변수.replaceAll(from, to)
// 문자열변수에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환

문자열변수.trim()
// 문자열 시작과 끝의 모든 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

문자열변수.trimStart()
// 문자열 시작의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

문자열변수.trimEnd()
// 문자열 끝의 공백문자(스페이스, 탭, 엔터 등)을 제거한 문자열 반환
~~~



#### 배열 (Array)

- 키와 속성들을 담고 있는 참조 타입의 객체(object)
- 순서를 보장하는 특징이 있음
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능
- 배열의 마지막 원소는 array.length - 1로 접근

~~~javascript
// 배열 관련 메서드 (기본)

배열변수.reverse()
// 원본 배열의 요소들의 순서를 반대로 정렬

배열변수.push(value)
// 배열의 가장 뒤에 요소(value) 추가

배열변수.pop()
// 배열의 마지막 요소 제거

배열변수.unshift(value)
// 배열의 가장 앞에 요소(value) 추가

배열변수.shift()
// 배열의 첫번째 요소 제거

배열변수.includes(value)
// 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

배열변수.indexOf(value)
// 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환
// 만약 해당 값이 없을 경우 -1 반환

배열변수.join(separator)
// 배열의 모든 요소를 연결하여 반환
// separator(구분자)는 선택적으로 지정가능하며, 생략 시 쉼표를 기본값으로 사용

//Spread operator(...)를 사용하면 배열 내부에서 배열 전개 가능
const array = [1, 2, 3]
const newArray = [0, ...array, 4]
console.log(newArray) // [0, 1, 2, 3, 4]
~~~

~~~javascript
// 배열 관련 메서드 (심화)

배열변수.forEach((element, index, array) => {
    // do something
})
// 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
// 콜백 함수는 3가지 매개변수로 구성
// element: 배열의 요소
// index: 배열 요소의 인덱스
// array: 배열 자체
// 반환 값이 없는 메서드

배열변수.map((element, index, array) => {
    // do something
})
// 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
// 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
// 기존 배열 전체를 다른 형태로 바꿀 때 유용

배열변수.filter((element, index, array) => {
    // do something
})
// 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
// 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
// 기존 배열의 요소들을 필터링할 때 유용

배열변수.reduce((acc, element, index, array) => {
    // do something
}, initialValue)
// 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
// 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
// acc : 이전 콜백 함수의 반환 값이 누적되는 변수
// initialValue : 최초 콜백함수 호출 시 acc에 할당되는 값, 기본값은 배열의 첫번째 값
// 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

배열변수.find((element, index, array) => {
    // do something
})
// 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
// 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
// 찾는 값이 배열에 없으면 undefined 반환

배열변수.some((element, index, array) => {
    // do something
})
// 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
// 모든 요소가 통과하지 못하면 거짓 반환
// 빈 배열은 항상 거짓 반환

배열변수.every((element, index, array) => {
    // do something
})
// 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환
// 하나의 요소라도 통과하지 못하면 거짓 반환
// 빈 배열은 항상 참 반환
~~~



#### 객체 (Objects)

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능, key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표('')로 묶어서 표현
- vaule는 모든 타입(함수포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
- 메서드는 객체의 속성이 참조하는 함수
- 객체.메서드명() 으로 호출 가능
- 메서드 내부에서는 this 키워드가 객체를 의미함

~~~javascript
const me = {
    firstName: 'John',
    lastName: 'Doe',
    getFullName: function () {
        return this.firstName + this.lastName
	}
}
~~~



#### JSON (JavaScript Object Notation)

- key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입이므로 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수
- 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공
  - JSON.parse()
    - JSON => 자바스크립트 객체
  - JSON.stringify()
    - 자바스크립트 객체 => JSON



### Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
  - 특정 메서드를 호출(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있음



#### addEventListener

~~~javascript 
//EventTarget.addEventListener(type, listener)

<body>
    <button id="btn">버튼</button>
    <script>
        const btn = doucment.querySelector('#btn') //id가 btn인 버튼을 변수btn에 할당
        btn.addEventListener('click', function() { 
            console.log('버튼 클릭!')
        }) // 버튼이 클릭될 때마다 '버튼 클릭!' 출력
    </script>
</body>
~~~

~~~javascript
<body>
  <h2>Change my color</h2>
  <label for="change-color-input">원하는 색상을 영어로 입력하세요.</label>
  <input type="text" id="change-color-input">
      
  <script>
    const colorInput = document.querySelector('#change-color-input')
    colorInput.addEventListener('input', function(event) {
      const h2Tag = document.querySelector('h2')
      h2Tag.style.color = event.target.value 
      // 중요! h2 태그 스타일에 color = '입력값'을 대입한다.
    })
  </script>
</body>
~~~



#### Event 취소

- event.preventDefault()
- 현재 이벤트의 기본 동작을 중단
- HTML 요소의 기본 동작을 작동하지 않게 막음
  - ex)  a 태그의 기본 동작은 클릭 시 링크로 이동 / form 태그의 기본 동작은 form 데이터 전송
- 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

~~~javascript
<body>
  <input type="checkbox" id="my-checkbox">
  <script>
    const checkBox = document.querySelector('#my-checkbox')
    checkBox.addEventListener('click', function(event) {
      event.preventDefault() //체크박스 클릭시 아무일도 일어나지 않음
      console.log(event)
    })
  </script>
</body>
~~~



#### 클래스를 조작하는 방법

태그의 클래스에 

- 태그.classList.add() : 새로운 클래스를 추가하거나,
- 태그.classList.remove() : 기존에 있던 클래스를 제거하거나
- 태그.classList.replace() : 기존에 있던 클래스를 새로운 클래스로 대체하거나,
- 태그.classList.toggle() : 있다면 제거하고, 없다면 추가할 수 있다. (클래스 on / off )



#### input 값을 가져오는 방법

~~~javascript
<body>
    <input type="password" name="password" id="password">
	<script>
		const password = document.querySelector('#password').value
		// 인풋 태그에 .value를 붙히면 인풋에 입력된 값을 가져올 수 있다.
	</script>
</body>
~~~

