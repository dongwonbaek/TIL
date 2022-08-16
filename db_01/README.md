# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```

```
COUNT(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
```

```
COUNT(*)
--------
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 AND is_drinking = 1;
-- 두개의 조건을 걸기 위해서 콤마, WHERE 한번 더, AND 사용해봤는데 AND만 가능하군요
```

```
COUNT(*)
--------
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
sqlite> SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 and va_right >= 2.0; 
-- and가 소문자로도 가능하네요
```

```
COUNT(*)
--------
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
-- 중복은 DISTINCT
```

```
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

### 허리 둘레가 90이상이면서 몸무게가 70이하인 사람
```sql
SELECT COUNT(*) FROM healthcare WHERE waist >= 90 and weight <= 70;
```
```
COUNT(*)
--------
78560
```


### 흡연 또는 음주를 하는 사람 수를 출력하시오
```sql
SELECT COUNT(*) FROM healthcare WHERE smoking > 1 or is_drinking > 0;
-- smoking 값의 default가 1인 것 같다.
-- 
```
```
COUNT(*)
--------
661970
```

### 흡연 또는 음주를 하는 사람 중에 혈압이 140 이상인 사람 수를 출력하시오
```sql
SELECT COUNT(*) FROM healthcare WHERE (smoking > 1 or is_drinking > 0) and blood_pressure >= 140;
-- 혈압이 140 이상이면 고혈압이라고 한다.
```
```
COUNT(*)
--------
87712
```
