

# 파이썬(Python)✔

- 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않음
- 문법표현이 매우 간결하여 프로그래밍 경험이 없어도 짧은 시간 내에 마스터할 수 있음
- 같은 작업에 대해서도 C나 자바로 작성할 때 보다 간결하게 작성 가능
- 원도우즈, 맥OS, 리눅스, 유닉스 등 다양한 운영체제에서 실행가능
- 동적 프로그래밍 언어
- 객체지향 언어



## 변수란?

- 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에, 즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수'라고 불림

- 변수 이름은 

  - 숫자로 시작하면 안되고

  - 예약어와 같은 이름은 사용하면 안되고

  - 알파벳은 대소문자를 구별하며, 

  - 언더바(_)와 숫자는 사용할 수 있다.



코드는 

1. 위에서 아래로
2. 오른쪽에서 왼쪽 

순서로 읽어야 한다.



(=)연산자는 할당의 의미이다. 수학의 '같다' 의미와는 전혀 다르다.



주석

주석으로 처리될 내용 앞에 '# '을 입력



## 자료형 분류

- 불린형(Boolean Type)
  - True / False 값을 가진 타입은 bool
  - 비교/논리 연산을 수행함에 있어서 활용됨
  - 다음은 모두 False로 변환 (0, 0.0, (), [], {}, ", None)
- 수치형(Numeric Type)
  - int(정수, integer)
  - float(부동소수점, 실수, floating point number)
  - complex(복소수, complex number) (잘안쓰임)
- 문자열(String Type)
- None



## 산술 연산자

| 연산자 | 내용     |
| ------ | -------- |
| +      | 덧셈     |
| -      | 뺼셈     |
| *      | 곱셈     |
| %      | 나머지   |
| /      | 나눗셈   |
| //     | 몫       |
| **     | 거듭제곱 |



## 비교 연산자

| 연산자   | 내용                          |
| -------- | ----------------------------- |
| <        | 미만                          |
| <=       | 이하                          |
| >        | 초과                          |
| >=       | 이상                          |
| ==       | 같음                          |
| !=       | 같지않음                      |
| *is*     | *객체 아이덴티티(OOP)*        |
| *is not* | *객체 아이덴티티가 아닌 경우* |



### 문자열(String Type)

- 모든 문자는 str타입

- 문자열은 작은 따옴표(')나 큰 따옴표(") 사용



### 중첩따옴표

- 따옴표 안에 따옴표를 표현할 경우

- 작은 따옴표가 들어 있는 경우는 큰 따옴표로 문자열 생성

- 큰 따옴표가 들어 있는 경우는 작은 따옴표로 문자열 생성



### 삼중따옴표

- 작은 따옴표나 큰 따옴표를 삼중으로 사용

- 따옴표 안에 따옴표를 넣을 때, 여러줄을 따옴표 안에 넣을 때

```python
print('''문자열 안에 작은 따옴표'나 "큰 따옴표"를 사용할 수 있고 여러 줄을 사용할 때도 편리하다. ''')
```



# 슬라이싱



**컴퓨터에서는 숫자를 0부터 센다.**

```python
fruit = 'abcde'
print(fruit[1])
```

b가 출력된다.



```python
print(fruit[1:3])
```

1이상 3미만의 뜻이다. bc가 출력된다.



마지막 숫자를 출력하기 위해서는 -1을 넣으면 된다.

```python
print(fruit[-1])
```



:3 <- 앞 숫자가 생략되면 0이 생략된것이다. 처음부터 3까지 라는 뜻이고,

 5: 처럼 반대로 사용되면 5부터 마지막 까지의 뜻

:: 는 처음부터 끝까지 1step 으로 표현

::-1 은 반대로, 끝부터 처음까지 1step으로 표현



## 문자열 안에 변수 넣기

```python
score = 100
print(f'내 점수는 {score}이야.')

pi = 3.14
r = 2
print(f'원주율은 {pi}이고, 원 넓이는 {pi*r*r}이야.')
```

f를 넣고 {}중괄호로 변수를 감싸주면 된다!



문자열 특징

- 변경 불가능함
- 반복 가능함



컨테이너 정리

```python
students = ['동현', '효근', '수경', '나영', '다겸', '예지']
print(students[0])
print(students[-1])
```

```python
# 딕셔너리
students = {
    '1회차': ['동현', '효근'],
    '2회차': ['수경', '나영'],
    '3회차': ['다겸', '예지']
}

print(students['1회차'])
```

***



### 시퀀스 : 순서가 있어서 인덱스로 접근가능

- #### 문자열: 문자들의 나열

  - 변경 불가능, 반복 가능

  

- #### 리스트: 변경 가능한 값들의 나열

  - 변경 가능, 반복 가능
  - []대괄호 또는 list()로 생성
  - 값추가는 .append(), 값 삭제는 .pop()

  

- #### 튜플: 변경 불가능한 값들의 나열

  - 변경 불가능, 반복 가능
  - ()소괄호 또는 tuple()로 생성

  

- #### 레인지: 숫자의 나열

  - 변경 불가능, 반복 가능
  - range(n): 0부터 n-1까지
  - range(n, m): n부터 m-1까지
  - range(n, m, s): n부터 m-1까지 s만큼 증가시키며 나열

  

### 컬렉션/비시퀀스: 순서가 없음

- #### 세트: 유일한 값들의 모음

  - 변경 가능, 반복 가능
  - 순서가 없고 중복된 값이 없음
  - {}중괄호 또는 set()로 생성
  - 인덱스로 접근 X
  - 값 추가는 .add() , 값 삭제는 .remove()

  

- #### 딕셔너리: 키-값들의 모음

  - 키-값이 쌍으로 이뤄진 모음. 이때 키는 불변 자료형만 가능하고 값은 어떠한 형태든 상관 없음
  - 키와 값은 :로 구분되고 개별 요소는 ,로 구분
  - 변경 가능, 반복 가능
  - 키 삭제는 .pop()
  
  

***



# 조건문✔

~~~python
a = -10
if a >= 0;
	print('양수')
else:
    print('음수')
print(a)
~~~

## 복수 조건문

~~~python
dust = 80
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
print('미세먼지 확인 완료')
~~~

## 중첩 조건문

~~~python
dust = -10
if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요.')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust >= 0:
        print('좋음')
    else:
        print('값이 잘못되었습니다.')
~~~

## 조건 표현식

~~~python
value = num if num >= 0 else -num
# value에 num을 대입한다, num이 0보다 크거나 같다면.
# num이 0보다 크거나 같지 않다면, value에 -num을 대입한다.
# 절대값 산출을 위한 코드
~~~



# 반복문✔

- **while문**

  ~~~python
  while <expression>:
      # Code block
  ~~~

  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행.
  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행.
  - 무한 동작을 하지 않도록 종료조건이 필요.

  

- **for문**

  ~~~python
  for <변수명> in <iterable>:
      # Code block
  ~~~

  - for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함
  - 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음
  - 딕셔너리 순회
    - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

## 반복문 제어

- **break**
  
  - 반복문을 종료
  
- **continue**
  
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
  
- **for-else**
  
  - 끝까지 반복문을 실행한 이후에 else문 실행
  - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음
  
  

***



# 함수✔

- 함수의 선언은 **def** 키워드를 활용함
- 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함
- 함수는 parameter를 넘겨줄 수 있음
  - parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
  - argument : 함수를 호출할 때, 넣어주는 값
- 함수는 동작 후에 return을 통해 결과값을 전달함
- 함수는 함수명()으로 호출
- 함수는 반드시 값을 하나만 return 하고 return과 동시에 실행이 종료됨.



**함수의 결과값은 항상 하나이지만 예외가 있다.**

~~~python
def minus_and_product(x, y):
    return x - y, x * y
print(minus_and_product(x, y))
# (-1, 20) << 함수의 return 값이 콤마로 구분된 2개의 값이면 두 값을 묶어 튜플로 반환된다.
~~~



### Argument

- 함수 호출 시 함수의 parameter를 통해 전달되는 값
- Argument는 소괄호 안에 할당 func_name(argument)
- 필수 Argument : 반드시 전달되어야 하는 argument
- 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달



#### Positional arguments

- 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

~~~python
def add(x, y):
    return x + y
print(add(2, 3)) # 자동으로 위치에 따라, x에 2를 대입, y에 3을 대입
~~~



#### Keyword arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- Keyword Argument 다음에 Positional Argument를 활용할 수 없음

~~~python
def add(x, y):
    return x + y
add(x=2, y=5)	# 가능
add(2, y=5)		# 가능
add(x=2, 5)		# 불가능, Keyword Argument(x=2)가 먼저 제시되었으므로. 
~~~



#### 정해지지 않은 개수의 arguments

- 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
  - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용
- Argument들은 튜플로 묶여서 처리되며, parameter에 *를 붙여 표현

~~~python
def add(*args):
    for arg in args:
    print(arg)
# add(2)
# add(2, 3, 4, 5) 등 다양한 상황에서 활용할 수 있다.
~~~



#### 정해지지 않은 개수의 keyword arguments

- 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정
- Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

~~~python
def family(**kwargs):
    for key, value in kwargs:
        print(key, ":", value)
family(father='John', mother='Jane', me='John Jr.')
~~~



#### 객체 수명주기

객체는 각자의 수명주기가 존재

- built-in scope : 파이썬이 실행된 이후부터 영원히 유지
- global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때 까지 유지
- local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지



### 내장 함수 응용(map)

map(function, iterable)

- 순회가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
- 단 결과값은 map object로 반환되기 때문에 형변환을 통하여 원하는 모습으로 확인할 수 있음

~~~python
 n, m = map(int, input().split())
~~~

~~~python
numbers = [1, 2, 3]
result = map(str, numbers)
print(list(result))
#['1', '2', '3']
~~~



![img](python.assets/unknown.png)



***



# 메서드✔



## 리스트 메서드



**'word'.find('w')** 

w의 첫 번째 위치를 반환, 없으면 -1 반환

**'word'.index('w')**

w의 첫 번째 위치를 반환, 없으면 오류 반환



`is가 붙은 메서드는 True/False 값만 반환`

**.isalpha()** 문자인가?

**.isupper()** 전부 대문자인가?

**.islower()** 전부 소문자인가?



**.replace('a', 'b')** 

모든 a를 b로 바꿔서 반환



**.replace('a', 'b', 2)** 

가장 앞에 있는 a 2개를 b로 바꿔서 반환



**.strip()** 

괄호 안 문자열을 지정하지 않으면 공백 제거. 공백은 space 나 '\n'도 포함



**.lstrip()** 

왼쪽만 제거



**.rstrip()** 

오른쪽만 제거



**.split()** 

문자열을 특정한 단위로 나눠 리스트로 반환



**' '.join()** 

괄호 안 문자열을 ' '안의 seperator로 합쳐 하나의 문자열로 반환. 괄호 안에는 문자열만 가능.



### 추가

**.append(x)** 

리스트에 값을 추가함. 반환값은 None



**.extend(['a', 'b'])** 

리스트에 리스트를 추가함 (괄호안의 값은 리스트로 작성되어야 한다.)



**.insert(i, x)** 

정해진 위치 i에 x를 추가함



### 제거

**.remove(x)** 

리스트에서 값이 x인 것 삭제. 리스트에 x 가 없으면 오류 출력



**.pop(i)** 

정해진 위치 i에 있는 값을 삭제하고 그 항목을 반환. i가 지정되지 않으면, 마지막 항목을 삭제하고 반환



**.clear()** 

모든 항목 삭제



### 탐색 및 정렬

**.index(x)** 

x값을 찾아 해당 index 값을 반환. index 값의 자료형은 int 



**.count(x)** 

원하는 값의 개수를 반환



**.sort()** 

원본 리스트를 정렬함. None을 반환



**.reverse()** 

순서를 반대로 뒤집음. None을 반환

~~~python
a = [10, 1, 100]
new_a = a.sort()
print(a, new_a)
# [1,10, 100] None
# 리스트 메서드 활용
# 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경
# return되는 것은 None

b = [10, 1, 100]
new_b = sorted(b)
print(b, new_b)
# [10, 1,100] [1, 10, 100]
# 리스트에 sorted 함수를 활용
# sorted 함수를 활용하면, 원본을 변경하지 않음
# return 되는 것은 정렬된 리스트
~~~




`문자열의 메서드는 return 값이 문자열이고 리스트의 메서드는 return 값이 None이다.`

`그 이유는 문자열은 바뀔 수 없고, 리스트는 바뀔 수 있게 때문이다.`

 

## 딕셔너리 메서드

### 조회



**.get(key,[default])** 

key를 통해 value 를 가져옴. default 값을 설정할 수 있음(기본: None) 에러는 발생하지 않음



**.pop(key, [default])** 

key가 딕셔너리에 있으면 제거하고 해당 값을 반환. 없으면 default를 반환. default 값이 없으면 key error 발생



**.update([other])** 

값을 제공하는 key, value로 덮어씀



**.items()** 

일종의 리스트 안에, key, value로 구성된 tuple로 구성됨



**딕셔너리.keys()** 

키만 리스트로 출력



**딕셔너리.value()** 

value만 리스트로 출력



- import json 다른 json파일의 내용물을 현재 파일로 가져올 때 사용한다.
- import pprint `print() 대신 pprint()를 사용하면, 결과문을 이쁘게 정렬한다.
- f = open('파일명.json', 'r', encoding = 'utf-8') 파일명.json 이라는 파일 내용을 읽기 전용으로 연다.
- 변수 = json.load(f) 변수에 f에 열린 파일내용을 할당한다. 변수에 할당된 내용은 파일명.json 내용과 동일하다.



## 오류 통제

~~~python
number = input()
try:
  print(100/int(number))
except ZeroDivisionError:
  print('0으로 나눌 수는 없습니다.')
except ValueError:
  print('숫자 형식을 입력해주세요.')
except Exception:
  print('오류')
~~~



# 객체 지향 프로그래밍(Object Oriented Programming)🔍

- 파이썬은 모든 것이 객체(object)

- 컴퓨터 과학에서 객체 또는 오브젝트는 클래스에서 정의한 것을 토대로 메모리에 할당된 것으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료 구조, 함수 또는 메소드가 될 수 있다.

- 객체 지향 프로그래밍은 컴퓨터 프로그래밍의 패러다임 중 하나이다. 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.

- 대상의 정보와 동작 ( 주어 + 동사 )



### **객체는 특정 타입(class)의 인스턴스이다.**

- 234, 900, 5 는 모두 int의 인스턴스

- 'hello', 'bye'는 모두 string의 인스턴스

- [232, 89, 1], []은 모두 list의 인스턴스



### **객체의 특징**

- 타입: 어떤 연산자와 조작이 가능한가?
- 속성: 어떤 상태를 가지는가?
- 조작법: 어떤 행위를 할 수 있는가?



### **객체지향 프로그래밍이란?**

프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법



~~~python
class MyClass: 
    pass
# 클래스 정의할 때는 대문자를 섞는 것이 일반적이고,(CamelCase)
# 변수를 정의할 때는 소문자만 쓰는 것이 일반적이다.(snake_case)
~~~



```python
class Person:
    
    # 사람이라면 이름을 가지고 있다.
    # 인스턴스를 만들 때는 이름 정보를 받아서 하고 싶다.
    
    def __init__(self, name):
        # 개별 인스턴스에 각각 name 속성을 지정
        self.name = name
	
    # self : 호출하는 인스턴스를 파이썬 내부적으로 전달해줌
    def greeting(self):
        print(f'안녕하세요, {self.name}입니다.')
        
jimin = Person('지민')
print(jimin.name)	# 지민
jimin.greeting() # Person.greeting(jimin)

iu = Person('지은')
print(iu.name)
iu.greeting()
```



### 인스턴스와 클래스 간의 이름공간

- 클래스를 정의하면, 클래스와 해당하는 이름공간 생성

- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름공간 생성

- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색



**클래스 메소드**

클래스가 사용할 메소드

@classmethod 데코레이터를 사용하여 정의

- 데코레이터: 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

호출 시, 첫번째 인자로 클래스(cls)가 전달됨



**스태틱 메소드**

인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

속성을 다루지 않고 단지 기능만을 하는 메소드를 정의할 때, 사용

@staticmethod 데코레이터를 사용하여 정의

호출시 어떤 정의도 전달되지 않음



```python
class MyClass:
    class_variable = '클래스변수'
    
    #메서드들을 정의했습니다.
    def __init__(self):
        self.instance_variable = '인스턴스 변수'
    
    # 인스턴스 메서드 정의
    def instance_method(self):
        return self, self.instance_variable
    
    # 클래스 메서드 정의 / 클래스 내에 클래스를 정의할 때
    @classmethod # 데코레이터: 함수를 꾸며주는 것인데 지금은 고민하지 말기.
    def class_method(cls):
        return cls, cls.class_variable
    
    # 스태틱 메서드 정의 / 클래스 내에 클래스나 인스턴스가 필요없는 메서드가 필요할 때
    @staticmethod # 데코레이터
    def static_method():
        return '스태틱'
    
c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메서드 호출', c1.instance_method())
print('클래스 메서드 호출', c1.class_method())
print('스태틱 메서드 호출', c1.static_method())
```



# 다양한 응용 문법📖

### lambda

#### lambda[parameter] : 표현식

- 람다함수

  : 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림

- 특징
  - return문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용가능



## 파이썬 패키지 관리자(pip)

PyPI 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리시스템

패키지 설치 명령어

```bash
$ pip install SomePackage
# 패키지 설치

$ pip install SomePackage==1.0.5
$ pip install 'SomePackage>=1.0.4'
# 패키지 특정 버전 설치

$ pip uninstall SomePackage
# 패키지 삭제

$ pip list
# 설치되어 있는 패키지 목록 출력

$ pip freeze
# 설치된 패키지 목록을 pip install 로 활용할 수 있는 형식으로 출력하여
# requirements.txt 폴더에 저장하여 개발자들끼리 공유할 때 사용한다.
# 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함(관습)

$ pip install -r requirements.txt
# requirements.txt에 기록되어있는 패키지 목록들을 그대로 설치한다.
```





### 입력값을 외부 파일에서 끌어오기

~~~python
import sys
sys.stdin = open('input.txt')

# 같은 폴더 내의 파일만 가능
~~~

