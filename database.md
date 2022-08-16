# 데이터베이스



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



**sqlite 명령어**

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

