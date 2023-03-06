-- SET @변수이름 = 변수의 값;
-- SELECT @변수이름;
USE market_db;
SET @myVar1 = 5;
SET @myVar2 = 4.25;

SELECT @myVar1;
SELECT @myVar2;
SELECT @myVar1 + @myVar2;

SET @txt = '가수 이름 ==> ';
SET @height = 166 ;
SELECT @txt, mem_name FROM member WHERE height > @height ORDER BY height;

-- 아래 형식은 불가능하다. LIMIT에는 변수를 사용할 수 없기 때문이다.
-- SET @count = 3;
-- SELECT mem_name, height FROM member ORDER BY height LIMIT @count;

-- PREPARE 실행하지 않고 SQL 문만 준비
-- EXECUTE 에서 실행
SET @count = 3;
PREPARE mySQLvariable FROM 'SELECT mem_name, height FROM member ORDER BY height LIMIT ?';
EXECUTE mySQLvariable USING @count;