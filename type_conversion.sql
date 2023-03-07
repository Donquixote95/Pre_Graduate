USE market_db;

-- type conversion ; 문자형을 정수형으로 바꾸거나, 반대로 하는 것
-- explicit conversion ; 직접 함수를 변환해서 형 변환
-- implicit conversion ; 별도의 지시 없이 자연스럽게 변환되는 형 변환

-- 명시적인 변환
-- CAST(), CONVERT() 는 형태만 다를 뿐 동일한 기능을 한다.

SELECT AVG(price) AS '평균 가격' FROM buy; -- 결과가 실수로 나온다.
SELECT CAST(AVG(price) AS SIGNED) '평균 가격' FROM buy; -- SIGNED는 부호가 있는 정수
SELECT CONVERT(AVG(price), SIGNED) '평균 가격' FROM buy; -- 위와 동일

-- 다양한 구분자를 날짜형으로 변경하기
SELECT CAST('2023$12$12' AS DATE);
SELECT CAST('2023/12/12' AS DATE);
SELECT CAST('2023%12%12' AS DATE);
SELECT CAST('2023@12@12' AS DATE);

-- CONCAT() 함수는 문자를 이어주는 역할을 한다.
SELECT num, 
	   CONCAT(CAST(price AS CHAR), 'X', CAST(amount AS CHAR), '=')'가격X수량', 
	   price*amount '구매액'
	FROM buy ; 


-- 암시적인 변환
SELECT '100' + '200'; -- 문자를 더했지만, 문자는 더할 수 없으므로 자동으로 숫자 100, 200으로 변환해서 덧셈을 수행한다.
SELECT CONCAT('100', '200'); -- CONCAT 함수를 사용해야 문자 '100'과 문자 '200'을 연결할 수 있다.

SELECT CONCAT(100, '200'); -- 이 경우 숫자 100이 문자 100으로 변환되어 위 결과와 같다.
SELECT 100 + '200'; -- 이 경우 문자 200이 숫자 200으로 자동 변환되어 300이 출력된다.