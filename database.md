

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

- 정규화