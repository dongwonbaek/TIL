

# 데이터베이스



~~~
팁박스 (실습진행하며 깨달았던 것들)
- WHERE 문에서 NULL값을 조건으로 탐색할때 등호 ( = )를 사용해서 비교하면 안된다. IS NULL 이나 IS NOT NULL을 사용해야함.
- 정렬기준(ORDER BY문)이 여러개일 경우 콤마를 사용해 구분하고, 각 조건마다 오름차순, 내림차순 여부를 붙혀야 함.
- strftime(%Y, 칼럼명) 은 칼럼이 날짜형식일 경우 년도를 출력한다. %m 은 월, %d 는 일을 출력하고 함께 출력도 가능하다. SELECT, WHERE 뒤에 사용가능
~~~



데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성(정확한 정보를 보장)



관계형 데이터베이스(RDB)

- 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
- 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스



스키마

- 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것



테이블

- 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합



기본키(Primary Key): 각 행(레코드)의 고유 값

- 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨
- 절대로 중복이 생기지 않음



관계형 데이터베이스 관리 시스템(RDBMS)

- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미
- My SQL, Oracle, MS SQL, SQLite 등



SQLite

- 서버 형태가 아닌 **파일 형식**으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 스프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능



SQL (Structured Qurery Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
- DDL - 데이터 정의(Definition) 언어 : 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
- DML - 데이터 조작(Manipulation) 언어: 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
- DCL - 데이터 제어(Control) 언어: 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어

`csv(Comma Seperated Variables) : 콤마로 구분된 값들`



**sqlite3 명령어**

~~~sqlite
.mode csv -- csv파일을 테이블로 가져올 수 있는 모드 실행
.import hellodb.csv examples -- hellodb.csv 라는 파일을 examples이라는 이름의 테이블로 생성
.tables -- 현재 존재하는 테이블 검색
.headers on -- 데이터 출력시 열 이름을 위에 같이 출력
.mode column -- 열 이름 출력시 데이터와 --으로 구분지음
~~~



데이터베이스 생성 및 스키마 정의

~~~sqlite
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT,
age INT DEFAULT 1 CHECK (0 < age)
-- 기본값은 1이되, 0보다 큰 값으로만 구성되어야 한다.
address TEXT
);
~~~



데이터 삽입

~~~sqlite
INSERT INTO classmates VALUES ( 1, '조세호')
~~~



데이터 조회

~~~sqlite
SELECT * FROM classmates;
~~~



테이블 삭제

~~~sqlite
DROP TABLE classmates;
~~~



필드 제약 조건

- NOT NULL : NULL 값 입력 금지
- UNIQUE: 중복 값 입력금지(NULL 값은 중복 입력 가능)
- PRIMARY KEY: 테이블에서 반드시 하나, NOT NULL + UNIQUE
- FOREIGN KEY: 외래키, 다른 테이블의 Key
- CHECK: 조건으로 설정된 값만 입력 허용
- DEFAULT: 기본 설정 값



**INSERT**

- 테이블에 단일 행 삽입
  - INESRT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
- 테이블에 정의된 모든 컬럼



**classmates 테이블을 만들고 이름이 홍길동이고 23살인 데이터를 넣고 조회해보자**

~~~sqlite
CREATE classmates(
name TEXT,
age INTEGER,
address TEXT DEFAULT '대한민국'
-- DEFAULT 뒤 숫자나 문자는 기본값으로 설정되는 값이다.
);

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;
-- id 값은 rowid 라는 것을 통해 primary key가 지정되지 않은 경우 자동으로 id를 정해준다.
-- * 은 모든 값을 의미함.
~~~

~~~sqlite
CREATE TABLE classmates(
	name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'),
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');
-- 입력할 데이터가 여러개일 경우 위와 같은 방법으로 입력할 수 있다.
~~~

~~~sqlite
CREATE TABLE members(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);
-- AUTOINCREMENT를 사용하면, 데이터 삭제 시 삭제된 ID를 다시 재사용할 수 없게 만든다. 상황에 따라서 적절하게 활용할 수 있다.
-- 이 때는 rowid를 사용할 수 없다.
~~~



**SELECT**

- 테이블에서 데이터를 조회
- SELECT 문은 SQLite 에서 가장 기본이 되는 문이며 다양한 절과 함께 사용

~~~SQLite
SELECT rowid, name FROM classmates;
-- 특정 컬럼 값만 조회

SELECT rowid, name FROM classmates LIMIT 1;
-- rowid와 name 값을 한 명만 조회

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- 3번쨰 id를 조회,
-- OFFSET 뒤 숫자는 그만큼 건너뛴 값을 조회한다는 뜻

SELECT * FROM classmates WHERE address='서울';
-- 주소가 서울인 사람들을 조회

SELECT DISTINCT age FROM classmates;
-- classmates 테이블에서 age 값을 중복을 제거하고 조회
~~~



**DELETE**

~~~SQLITE
DELETE FROM classmates WHERE rowid = 5;
-- rowid가 5인 데이터를 삭제
~~~



**UPDATE**

~~~SQLITE
UPDATE classmates SET address='서울' WHERE rowid=5
-- 어떻게 변경할 것인지를 SET 뒤에, 무엇을 변경할 것인지를 WHERE 뒤에 선언한다.
~~~



**WHERE 절에서 사용할 수 있는 연산자**

**=**, !=, ^=, <>,  >, >=, <, <=, AND, OR, NOT

`SQL에서의 = 는 파이썬의 == 와 같다. != ^= <> 는 모두 같은 뜻이다.`

- BETWEEN 값1 AND 값2
  - 값1과 값2 사이의 비교 (값1 <= 비교값 <= 값2)
- IN (값1, 값2, ..)
  - 목록 중에 값이 하나라도 일치하면 성공



**연산자 우선순위**

1. 괄호()
2. NOT
3. 비교연산자, SQL
4. AND
5. OR



**CSV 파일로 테이블 만들기**

1. CREATE 로 테이블 생성 및 스키마 작성

2. 데이터를 추가
   ​	.mode csv

3. 같은 디렉토리에 있는 users.csv 파일을 users 테이블로

   ​	.import users.csv users



### **Aggregate function(집계 함수)**

- 값 집합에 대한 계산을 수행하고 단일 값을 반환
- 여러 행으로부터 하나의 결괏값을 반환하는 함수
- SELECT문에서만 사용됨
  - COUNT() : 항목 개수
  - AVG() : 평균
  - MAX() : 최대값
  - MIN() : 최소값
  - SUM() : 합



**LIKE**

- 패턴 일치를 기반으로 데이터를 조회하는 방법 ( ex. LIKE '김%' )
- wildcards 종류
  - **%**: 0개 이상의 문자 (이자리에 문자가 있을 수도 있고 없을 수도 있다.)
  - **_** : 임의의 단일 문자 (이자리에 반드시 한개의 문자가 있어야 한다.
- 사용예시
  - LIKE ' 2\_%\_%' : 2로 시작하고 적어도 3자리인 값



**ORDER BY**

- 조회 결과 집합을 정렬
- SELECT 문에 추가하여 사용
- 정렬 순서를 위한 2개의 KEYWORD 제공
  - ASC - 오름차순(default)
  - DESC - 내림차순
- 사용예시

~~~sqlite
-- 나이 오름차순 정렬 후 상위 10명 조회
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;

-- 나이, 성 순으로 오름차순 정렬 후 상위 10명 조회
SELECT first_name FROM users ORDER BY age, last_name LIMIT 10;
-- 정렬은 오름차순이 기본으로 설정되어있기 때문에 정렬방식을 선택하지 않으면 자동으로 오름차순(ASC)이 된다.

-- 계좌 잔액 순 내림차순
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

-- 계좌 잔액 내림차순(높은 -> 낮은 것), 성 오름차순(ㄱ->ㅎ)
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
~~~



## 기본함수와 연산



### 문자열 함수

- SUBSTR(문자열, start, length): 문자열 자르기
  - 시작 인덱스는 1, 마지막 인덱스는 -1
- TRIM(문자열), LTRIM(문자열), RTRIM(문자열): 문자열 공백 제거
- LENGTH(문자열): 문자열 길이
- REPLACE(문자열, 패턴, 변경값): 패턴에 일치하는 부분을 변경
- UPPER(문자열), LOWER(문자열): 대소문자 변경
- ||: 문자열 합치기(concatenation)
- 사용예시

~~~sqlite
SELECT last_name||first_name 이름 FROM users LIMIT 5;
-- AS는 생략하고 띄어쓰기만 해도 된다.

SELECT LENGTH(first_name) 이름길이, first_name FROM users LIMIT 5;

SELECT REPLACE(phone,'-', '') FROM users LIMIT 5;
~~~



### 숫자 함수

- ABS(숫자): 절대 값
- SIGN(숫자): 부호 (양수 1, 음수 -1, 0 0)
- MOD(숫자1, 숫자2): 숫자1을 숫자2로 나눈 나머지
- CEIL(숫자): 올림
- FLOOR(숫자): 내림
- ROUND(숫자): 반올림
- 산술연산자: + - / * 전부 사용가능
- SQRT(숫자): 숫자의 제곱근
- POWER(숫자1, 숫자 2): 숫자1 ^ 숫자2



### GROUP BY

- SELECT 문의 optional 절

- 행 집합에서 요약 행 집합을 만듦

- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

- 반드시 WHERE절 뒤에서 사용

- **집계함수와 활용하였을 때 의미가 있음**

- **그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐**

- **GROUP BY 에서 활용하는 컬럼을 제외하고 집계함수를 써야 함. (집계함수 외 컬럼은 의미가 없음)**

- **GROUP BY는 결과가 정렬되지 않지만 기존 순서와는 다르게 바뀜**

  **그러므로 정렬해서 보고 싶다면 ORDER BY를 사용해야 함**

~~~SQLITE
SELCT AVG(나이) FROM users;

SELECT AVG(나이) FROM users GROUP BY 성;
-- 성씨 별로 평균나이를 출력

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-- 성씨 별로 몇명있는지 출력

SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
-- 조건에 따른 GROUP 하려면 HAVING을 쓴다.
~~~



### SELECT 문장 실행 순서 ✔

FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY => LIMIT/OFFSET

테이블을 대상으로 제약조건에 맞춰서 뽑아서 그룹화한다. 

그룹 중에 조건과 맞는 것 만을 조회하여 정렬하고 특정 위치의 값을 가져온다.



### ALTER TABLE

~~~sqlite
-- 1. 테이블 이름 변경
ALTER TABLE table_name 
RENAME TO new_name;

-- 2. 새로운 컬럼 추가 및 자료형 설정
ALTER TABLE table_name
ADD COLUMN column_definition TEXT DEFAULT 'hello';
-- 새로운 컬럼 추가시 자료형으로 NOT NULL을 지정할 수 없다.
-- 새롭게 생기는 컬럼 내에는 자료가 존재하지 않아 NULL상태로 생성되는데 
-- 이는 NOT NULL자료형에 해당할 수 없기 떄문이다.

-- 3. 컬럼 이름 수정
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;

-- 4. 컬럼 삭제
ALTER TABLE table_name
DROP COLUMN column_name;
~~~

---

### CASE

- SELECT 바로 뒤에서 사용됨
- CASE 문은 특정 상황에서 데이터를 변환하여 활용할 수 있음
- ELSE를 생략하는 경우 NULL값이 지정됨

~~~sql
SELECT
	id,
    CASE
        WHEN gender = 1 THEN '남성'
        WHEN gender = 2 THEN '여성'
        ELSE '중성'
    END AS 성별
FROM healthcare
LIMIT 5;
~~~

---

### 서브쿼리

- WHERE 에서의 활용

~~~SQL
SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users):
-- 쿼리 내 서브쿼리를 사용할 수 있다. 서브 쿼리는 ()괄호로 묶어주자.

-- 계좌잔고가 평균보다 높은 사람 수는?
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users):

-- users에서 유은정과 같은 지역에 사는 사람의 수는?
SELECT COUNT(*)
FROM users
WHERE sido = (SELECT sido FROM users WHERE first_name = 은정 AND last_name = 유);
~~~

- SELECT 에서의 활용

~~~sql
-- 전체인원과 평균 연봉, 평균 나이를 출력하세요.
SELECT COUNT(*) 전체인원수, AVG(연봉), AVG(age)
FROM users;
-- 서브쿼리 활용
SELECT
(SELECT COUNT(*) FROM users) AS 총인원,
(SELECT AVG(balance) FROM users) AS 평균연봉
(SELECT AVG(age) FROM users) AS 평균나이
FROM users;
~~~

- UPDATE 에서의 활용

~~~sql
UPDATE users
SET balance = (SELECT AVG(balance) FROM users):
~~~



다중행 서브쿼리

- 서브쿼리 결과가 2개 이상인 경우
- 다중행 비교 연산자와 함께 사용 (in, exists등)



다중칼럼 서브쿼리

~~~sql
-- 특정 성씨에서 가장 어린 사람들의 이름과 나이
SELECT last_name||first_name 이름, age 나이 
FROM users 
WHERE (last_name, age) 
	IN (
    	SELECT last_name, MIN(age) 
   	 	FROM users
   	 	GROUP BY last_name) 
ORDER BY last_name;
~~~



유저와 게시글	N : 1

게시글과 댓글	1 : N

유저와 좋아요	N : N

유저와 프로필	1 : 1

~~~sql
-- AC/DC 가 만든 앨범 제목 모두 출력
SELECT Title 
FROM albums 
WHERE ArtistsID = (SELECT ArtistsID FROM artists WHERE Name = 'AC/DC');
~~~

___



### JOIN

- 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
- 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합하여 출력하여 활용
- 일반적으로 레코드는 기본키나 외래키 값의 관계에 의해 결합함



**대표적인 JOIN**

- INNER JOIN: 두 테이블에 모두 일치하는 행만 반환

  - ```sql 
    SELECT * FROM users JOIN role ON users.role_id = role.id;
    
    SELECT * FROM users JOIN role ON users.role_id = role.id ORDER BY users.name DESC;
    -- 조인한 테이블에서 조건이나 정렬을 할 때는 테이블.칼럼명 으로 칼럼의 위치를 정확히 표기해주어야 함.
    ```

- OUTER JOIN: 동일한 값이 없는 행도 반환

  - ~~~sql
    SELECT * FROM articles LEFT OUTER JOIN users ON articles.user_id = users.id WHERE articles.user_id IS NOT NULL;
    -- 중복되는 데이터는 제거된다.
    ~~~

- CROSS JOIN: 모든 데이터의 조합

  - ~~~sql
    SELECT * FROM users CROSS JOIN role;
    -- 가능한 모든 경우를 출력
    ~~~

> INNER JOIN 과 LEFT OUTER JOIN의 차이점은 LEFT OUTER JOIN 은 NULL 값이 존재하면 같이 출력해주고, INNER JOIN은 그렇지 않다는 점이다.
>
> LEFT OUTER JOIN은 갖다 붙히기만 하는 것이고, INNER JOIN은 두 테이블의 교집합만 골라 합쳐서 출력한다.



### 모델링

- 데이터베이스의 구조나 형식으로 모델 구조만 보고 어떤 데이터를 다루는지 알 수 있음
- 개념적 데이터 모델링
  - 데이터의 요구사항을 찾고 분석하는 과정, 핵심 개체 사이의 관계를 찾아내고 표현
- 논리적 데이터 모델링
  - 데이터베이스 설계 프로세스의 과정으로 정보의 논리적인 구조와 규칙을 명확하게 표현하는 기법/과정
- 물리적 데이터 모델링
  - 논리적 데이터 모델이 데이터 저장소로서 어떻게 실제로 저장될 것인가
- ERD(Entity Relation Diagram) - 개체 관계 모델
- 관계
  - 카디널리티(Cardinality): 수적 관계
    - 1:1 관계 : A는 B를 하나 가진다. B는 A를 하나 가진다.
    - 1:N 관계 : A는 B를 여러 개 가진다. B는 A의 하나에 해당한다.
    - M:N 관계 : A는 B를 여러 개 가진다. B는 A를 여러 개 가진다.
  - 옵셔널리티
    - (1) 필수
    - (0) 선택



### 객체

`객체란 모든 것을 의미한다. 객체 내에는 속성과 메서드가 있고 속성의 객체 내의 값, 메서드는 객체 내에 존재하는 함수이다.`



### ORM

- Object - Relational - Mapping
- **객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술**
- 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크에서는 내장 Django ORM을 활용

모델 설계 및 반영

1. 클래스를 생성하여 내가 원하는 DB의 구조를 만든다.
2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 자동생성한다.
3. DB에 migrate 한다.

Migration

- Model에 생긴 변화를 DB에 반영하기 위한 방법
- 마이그레이션 파일을 만들어 DB 스키마를 반영한다.
- 명령어
  - makemigrations: 마이그레이션 파일 생성
  - migrate: 마이그레이션을 DB에 반영




~~~python
# python manage.py shell_plus 로 진입 (Django 내장 ORM)

Genre.object.create(name = "인디밴드")
genre = Genre.objects.get(id=1) #genre 라는 변수에 id가 1인 데이터를 할당
genre.name	# 그 데이터의 name 칼럼을 출력
'인디밴드'

Genre.objects.get(id=1)
# 반드시 하나이여야 함. 단일 객체로 출력, 많거나 없으면 오류 발생(PK로 조회할 때 사용)

Genre.objects.filter(id=1)
# 쿼리셋으로 출력, 여러개이거나 없어도 출력. 쿼리셋이라는 리스트로 출력(PK외의 것으로 조회할 때 사용)

genre = Genre.objects.get(id=2)  # (genre라는 변수에  id 가 2인 객체를 가쳐온다.)
genre.name #(가져온 객체의 name속성은?)
# '트로트'
genre.delete() #(장르에 할당된 객체를 삭제하여 반영한다.)
~~~

- **models.ForeignKey 필드**
  - 2개의 필수 위치 인자

    - Model class : 참조하는 모델
    - on_delete: 외래 키가 참조하는 객체가 삭제되었을 떄 처리 방식
      - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 떄 이를 참조하는 객체도 삭제 	

        ex)`글과 댓글의 관계`

      - PROTECT : 삭제되지 않음

      - SET_NULL : NULL 설정

      - SET_DEFAULT : 기본 값 설정
    - 사용예시 : **genre = models.ForeingKey('Genre', on_delete=models.CASCADE)** 
    - Genre라는 테이블의 기본키를 genre_id라는 외래키로 참조함. 삭제 시 같이 삭제

- **Foreign Key (외래키)**

  - 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
    - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

- **역참조(_set)**

  - genre = Genre.objects.get(id=1)

    genre.album_set.all()

    = id가 1인 장르를 가지고 있는 모든 앨범객체를 조회(역참조)



### Django 내장 QuerySet 메서드

1. **Select**

   - **[클래스명].objects.all()**

     : 해당 테이블 안에 있는 모든 데이터 조회하여 QuerySet 타입으로 반환

     ~~~bash
     # 테이블 내 모든 데이터를 조회
     In : Drink.objects.all()
     ~~~

     

   - **[클래스명].objects.get()**

     : 하나의 row만 조회. 주로 기본키 컬럼으로 조회한다. 결과가 1건 이상일 때는 에러를 발생시킨다. `QuerySet 타입이 아닌 객체 타입으로 반환한다는 점 주의.`

     ~~~bash
     # PK가 1인 데이터만 조회
     In : Drink.objects.get(id=1)
     ~~~

     

   - **[클래스명].objects.filter()**

     : 특정 조건에 맞는 row만 조회하고 싶을 때 사용한다. QuerySet 타입으로 반환.

     ~~~bash
     # category_id가 1인 데이터만 조회
     In : Drink.objects.filter(category_id=1)
     ~~~

     

   - **[클래스명].objects.exclude()**

     : 특정 조건을 제외한 데이터만 조회하고 싶을 때 사용한다. QuerySet 타입으로 반환.

     ~~~bash
     # category_id = 1인 데이터를 제외한 모든 데이터 조회
     In : Drink.objects.exclude(category_id=1)
     ~~~

     

   - **Lookup filter**

     : filter(), exclude() 메서드에서 사용 가능한 내장 모듈로, 필드 별 구체적인 값에 대한 비교를 가능하게 하는 Django의 내장 모듈이다.

     - **__contains** : 특정 문자가 포함된 것을 찾을 때 사용(대소문자 구분)

       ~~~bash
       # english_name 컬럼에 'Blend'라는 단어가 들어간 데이터 조회(대소문자 구분)
       In : Drink.objects.filter(english_name__contains="Blend")
       ~~~

     - **__icontains** : 특정문자가 포함된 것을 찾을 때 사용(대소문자를 구분하지 않음)

       ~~~bash
       # english_name 컬럼에 'blend'라는 단어가 들어간 데이터 조회(대소문자를 구분하지 않음)
       In : Drink.objects.filter(english_name__icontains="blend")
       ~~~

     - **__startswith** : 특정문자로 시작하는 것을 찾을 때 사용

       ~~~bash
       # english_name 컬럼에 'Nitro'로 시작하는 문자열을 가진 데이터 조회(대소문자 구분)
       In : Drink.objects.filter(english_name__startswith="Nitro")
       ~~~

     - **__endswith** : 특정문자로 끝나는 것을 찾을 때 사용

       ~~~bash
       # english_name 컬럼에서 'Tea'로 끝나는 문자를 가진 데이터 조회(대소문자 구분)
       In : Drink.objects.filter(english_name__enswith="Tea")
       ~~~

     - **__lt** : 특정값 보다 작은 데이터만 조회(less than의 약자)

       ~~~bash
       # id가 3보다 작은 데이터만 조회
       In : Drink.objects.filter(id__lt=3)
       # lte는 3도 포함한다.
       ~~~

     - **__gt** : 특정값 보다 큰 데이터만 조회(greater than의 약자)

       ~~~bash
       # id가 3보다 큰 데이터만 조회(3포함 X)
       In : Drink.objects.filter(id__gt=3)
       # gte는 3도 포함한다.
       ~~~

     - **__isnull** : True로 지정 시 특정 필드 값이 null인 것만 조회

       ~~~bash
       # description 컬럼이 null인 것만 조회
       In : Drink.objects.filter(description__isnull=True)
       # description 컬럼이 null이 아닌 것만 조회
       In : Drink.objects.filter(description__isnull=False)
       ~~~

     - **__in** : 리스트 안에 지정한 문자열들 중에 하나라도 포함된 데이터를 찾을 때 사용(단, 문자열과 정확히 일치해야함)

       ~~~bash
       # english_name 필드에 'Malcha' 또는 'Nitro Cold Brew' 값이 있는 것만 조회
       In : Drink.obects.filter(english_name__in=['Malcha', 'Nitro Cold Brew'])
       ~~~

     - **\_\_year, \_\_month, \_\_day, \_\_date** : date 타입의 필드에서 특정 년(_\_year), 월(\_\_month), 일(\_\_day) 혹은 특정 날짜 (\_\_date: YY-MM-DD형식)의 데이터를 찾을 때 사용

       ~~~bash
       # pub_date 필드에서 년도가 2021인 것만 조회
       In : Question.objects.filter(pub_date__year='2021')
       ~~~
       
     - **__range** : sart_date 와 end_date 사이에 있는 날짜를 가진 pub_date 인스턴스를 조회

       ~~~bash
       # pub_date 필드에서 날짜가 start_date 와 end_date 사이에 있는 데이터만 조회
       In : Entry.objects.filter(pub_date__range=(start_date, end_date))
       ~~~

       

   - **AND (&)  /  OR (|)**

     : filter() 메서드 사용 시, 두개 이상의 조건을 AND 또는 OR을 이용하여 표현할 수 있다. 

     ~~~bash
     # AND 예시 (Drink테이블에서 id가 6보다 크고, korean_name이 '라임'을 포함하는 데이터만 출력)
     IN : Drink.objects.filter(id__gt=6) & Drink.objects.filter(korean_name__contains = '라임')
     
     # OR 예시 (Drink테이블에서 id가 6보다 크거나, korean_name이 '라임'을 포함하는 데이터만 출력)
     IN : Drink.objects.filter(id__gt=6) | Drink.objects.filter(korean_name__contains = '라임')
     ~~~

     

   - **[클래스명].objects.count()**

     : 쿼리셋에 포함된 데이터 개수를 리턴한다.

     ~~~bash
     # Drink 테이블에 몇 개의 데이터가 들어있는지 조회
     In : Drink.objects.count()
     Out : 8
     ~~~

     

   - **[클래스명].objects.exists()**

     : 해당 테이블에 데이터가 있는지 확인. 있으면 True, 없으면 False 반환.

     ~~~bash
     # Menu에 name이 '음료'인 데이터가 있으면 True, 없으면 False
     In : Menu.objects.filter(name="음료").exists()
     Out : True
     ~~~

     

   - **[클래스명].objects.values()**

     : QuerySet의 내용을 딕셔너리 형태로 반환한다. 인자값에 아무것도 넣지 않으면 해당 클래스의 모든 필드와 그 값을 보여주고, 인자값에 특정 필드를 입력하면 입력한 필드에 대한 값을 반환한다.

     ~~~bash
     # Menu 테이블의 모든 필드를 딕셔너리 형태로 반환
     In : Menu.objects.values()
     Out: <QuerySet [{'id': 1, 'name': '음료'}, {'id': 2, 'name': '푸드'}, {'id': 3, 'name': '상품'}, {'id': 4, 'name': '카드'}]>
     
     # Menu 테이블의 name 필드만 딕셔너리 형태로 반환
     In : Menu.objects.values('name')
     Out: <QuerySet [{'name': '음료'}, {'name': '푸드'}, {'name': '상품'}, {'name': '카드'}]>
     ~~~

     

   - **[클래스명].objects.values_list()**

     : values()와 같으나 QuerySet의 내용을 딕셔너리가 아닌 리스트 타입으로 반환

     ~~~bash
     In : Menu.objects.values_list()
     Out: <QuerySet [(1, '음료'), (2, '푸드'), (3, '상품'), (4, '카드')]>
     
     In : Menu.objects.values_list('name')
     Out: <QuerySet [('음료',), ('푸드',), ('상품',), ('카드',)]>
     ~~~

     
     
   - **[클래스명].objects.order_by()**

     : 특정 필드를 기준으로 정렬을 할 때 사용, 필드명 앞에 -가 붙으면 내림차순을 의미한다.

     ~~~bash
     # korean_name 필드를 기준으로 오름차순 정렬
     In : Drink.objects.order_by('korean_name')
     
     # korean_name 필드를 기준으로 내림차순 정렬, 두번째 기준은 id 필드
     In : Drink.objects.order_by('-korean_name', 'id')
     ~~~

     

   - **[클래스명].objects.first(), [클래스명].objects.last()**

     : 쿼리 셋 결과 중 가장 첫번째 row만 조회할 때 사용, 쿼리 셋 결과 중 가장 마지막 row만 조회할 때 사용. 둘다 객체 타입 반환.

     ~~~bash
     # 가장 첫번째 row만 조회
     In : Drink.objects.first()
     
     # 가장 마지막 row만 조회
     In : Drink.objects.last()
     ~~~

     

   - **[클래스명].objects.aggregate()**

     : django의 집계함수 모듈(Avg, Max, Min, Count, Sum 등)을 사용할 때 쓰이는 메소드, 집계함수들을 파라미터로 받는다. 딕셔너리 타입으로 반환한다. 

     ~~~bash
     # 집계함수를 사용하려면 import 해줘야 함
     In : from django.db.models import Max, Min, Avg, Sum
     
     # Nutrition 테이블의 id 컬럼과 one_serving_kcal 컬럼만 조회
     In : Nutrition.objects.values('id','one_serving_kcal')
     Out: <QuerySet [{'id': 1, 'one_serving_kcal': Decimal('75.00')}, {'id': 2, 'one_serving_kcal': Decimal('120.00')}]>
     
     # one_serving_kcal 값 모두 더하기
     In : Nutrition.objects.aggregate(Sum('one_serving_kcal'))
     Out: {'one_serving_kcal__sum': Decimal('195.00')}
     
     # one_serving_kcal컬럼에서 가장 큰 값과 가장 작은 값의 차이
     In : Nutrition.objects.aggregate(diff_kcal = Max('one_serving_kcal') - Min('one_serving_kcal'))
     Out: {'diff_kcal': Decimal('45.00')}
     
     # one_serving_kcal 컬럼 값들의 평균
     In : Nutrition.objects.aggregate(avg_kcal = Avg('one_serving_kcal'))
     Out: {'avg_kcal': Decimal('97.500000')}
     ~~~

2. **Insert**

   - **[클래스명].objects.create()**

     ~~~bash
     In : Nutrition.objects.create(one_serving_kcal=120, sodium_mg=70, saturated_fat_g=0, sugers_g=25, protein_g=1, caffeine_mg=35, drink_id=3, size="Tall(톨)", size_fluid_ounce=355, size_ml=12)
     ~~~

     

   - **[클래스명].objects.bulk_create()**

     : 여러 개의 objects를 한꺼번에 생성할 때 사용

     ~~~bash
     In : Nutrition.objects.bulk_create([
     Nutrition(one_serving_kcal = 5, sodium_mg = 5, saturated_fat_g = 0, sugers_g = 0, protein_g= 0, caffeine_mg = 245, drink_id = 2, size = 'Tall(톨)', size_fluid_ounce = 355, size_ml = 12),
     Nutrition(one_serving_kcal = 290, sodium_mg = 110, saturated_fat_g = 0.9, sugers_g = 57, protein_g = 8, caffeine_mg = 0, drink_id = 4, size = 'Tall(톨)', size_fluid_ounce = 355, size_ml = 12) 
     ])
     ~~~

     

   - **[클래스명].objects.get_or_create()**

     : 해당 테이블에 조건에 맞는 데이터가 이미 존재하면 get을 해오고, 없으면 create하는 메소드. 튜플 타입을 반환해주는데 get 또는 create한 객체 와 True/False 형식으로 반환해준다. 여기서 True/False는 이미 존재하는 데이터면(=get하는 경우) False, 없는 데이터면(=create하는 경우) True를 의미

     ~~~bash
     # 이미 존재하는 데이터를 get_or_create 했을 때
     In : Drink.objects.filter(korean_name='나이트로 쇼콜라 클라우드')
     Out: <QuerySet [<Drink: 나이트로 쇼콜라 클라우드>]>
     
     In : new_drink = Drink.objects.get_or_create(korean_name='나이트로 쇼콜라 클라우드')
     
     # 기존에 있는 데이터 반환
     In : new_drink
     Out: (<Drink: 나이트로 쇼콜라 클라우드>, False)
     
     # 없는 데이터를 get_or_create 했을 때
     In : Drink.objects.filter(korean_name='new')
     Out: <QuerySet []>
     
     In : new_drink
     Out: (<Drink: new>, True)
     
     # 새로 추가된 것을 확인할 수 있다.
     In : Drink.objects.filter(korean_name='new')
     Out: <QuerySet [<Drink: new>]>
     ~~~

     

3. **Update**

   - 업데이트 할 row를 변수에 저장하고 그 변수의 필드에 접근하여 값을 변경할 수 있음. (반드시 save()해줘야 저장됨)

     ~~~bash
     a = Drink.objects.get(id=8)
     
     In : a
     Out: <Drink: 라임패션티>
     
     # id가 8인 row의 description 컬럼 값을 'Lime Passion 2'로 업데이트
     In : a.description = "Lime Passion 2"
     
     # 변경사항 저장 >> 실제 DB에 적용됨
     In : a.save()
     
     # 결과 확인
     In : Drink.objects.values('id','description').filter(id=8)
     Out: <QuerySet [{'id': 8, 'description': 'Lime Passion 2'}]
     ~~~

     

   - [클래스명].objects.filter().update()

     ~~~bash
     # filter로 조건을 걸고(id=8) 그 row의 특정 컬럼(discription) 값을 update
     In : Drink.objects.filter(id=8).update(description = "Lime Passion 3")
     Out: 1
     
     # 결과 확인
     In : Drink.objects.values('id','description').filter(id=8)
     Out: <QuerySet [{'id': 8, 'description': 'Lime Passion 3'}]>
     ~~~

     

4. **Delete**

   - 삭제할 row를 변수에 저장하고 그 변수에서 delete()메서드로 데이터를 삭제한다.

     ~~~bash
     # 변수에 저장
     In : a = Menu.objects.get(id=5)
     
     # 삭제
     In : a.delete()
     Out: (1, {'products.Menu': 1})
     ~~~

     

