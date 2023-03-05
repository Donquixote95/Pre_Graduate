-- AUTO_INCREMENT 열을 정의할 때 1부터 증가하는 값을 입력해준다. INSERT 에서는 해당 열이 없다고 생각하고 입력하면 된다.
-- AUTO_INCREMENT로 지정하는 열은 반드시 PRIMARY KEY로 지정해줘야 한다.

CREATE TABLE practice2 (
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
    
INSERT INTO practice2 VALUES (NULL, '보핍', 25);
INSERT INTO practice2 VALUES (NULL, '슬링키', 22);
INSERT INTO practice2 VALUES (NULL, '렉스', 21);
SELECT * FROM practice2;

SELECT LAST_INSERT_ID(); -- table의 마지막 auto_increment 값을 리턴하는 함수

-- 만약 auto_increment로 입력되는 다음 값을 100부터 시작하게 바꾸고 싶다면 다음과 같이 한다.
-- ALTER TABLE 뒤에는 테이블 이름을 입력하고, 자동 증가를 100부터 시작하기 위해 AUTO_INCREMENT를 100으로 지정했다.
ALTER TABLE practice2 AUTO_INCREMENT = 100;
INSERT INTO practice2 VALUES (NULL, '재남', 35);
SELECT * FROM practice2;
DROP TABLE practice2;
-- DROP TABLE practice3;

-- 처음부터 입력되는 값을 1000으로 지정하고, 다음 값은 1003, 1006, 1009와 같이 3씩 증가하도록 설정하는 방법
-- 시스템 변수인 @@auto_increment_increment를 변경하면 된다.
CREATE TABLE practice3 (
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
ALTER TABLE practice3 AUTO_INCREMENT = 1000; -- 시작값을 1000으로 지정
SET @@auto_increment_increment = 3; -- 증가값을 3으로 설정
-- 시스템 변수 ; MYSQL에서 자체적으로 갖고 있는 설정값이 저장된 변수를 말한다. 
-- 시스템 변수 앞에는 @@이 붙는다. 
-- 시스템 변수의 값을 확인하려면 SELECT @@시스템변수;를 실행하면 된다
SELECT @@auto_increment_increment;
-- 만약 전체 시스템 변수의 종류를 알고 싶다면 SHOW GLOBAL VARIABLES;를 실행하면 된다.
SHOW GLOBAL VARIABLES;

INSERT INTO practice3 VALUES (NULL, '토마스', 20), (NULL, '제임스', 23), (NULL, '고든', 25);
SELECT * FROM practice3;

-- INSERT INTO ~ SELECT
-- 다른 테이블에 이미 데이터가 입력되어 있다면 위 구문을 사용해서 해당 테이블의 데이터를 가져와서 한 번에 입력할 수 있다.
-- SELELCT 문의 열 개수는 INSERT 할 테이블의 열 개수와 같아야 한다.
-- 즉, SELECT의 열이 3개라면 INSERT될 테이블의 열도 3개여야 한다.

DROP TABLE practice3;

SELECT COUNT(*) FROM world.city; -- MySQL을 설치할 때 함께 생성된 world 데이터베이스의 city 테이블의 개수를 조회
-- 데이터베이스_이름.테이블_이름 으로 다른 데이터베이스의 테이블에 접근할 수 있다.

-- DESC 명령
-- Describe의 약자로 테이블의 구조를 출력해주는 기능을 한다. 
DESC world.city;

SELECT * FROM world.city LIMIT 5;

CREATE TABLE city_popul (city_name CHAR(35), population INT);
-- DSEC 명령어로 확인한 것을 바탕으로 새로운 테이블을 만든다.

INSERT INTO city_popul
	SELECT Name, Population FROM world.city;
    
SELECT * FROM city_popul LIMIT 5;

-- UPDATE 
-- 기존에 입력되어 있는 값을 수정하는 명력
-- MySQL 워크벤치에서는 기본적으로 UPDATE 및 DELETE를 허용하지 않기 때문에 UPDATE를 실행하려면 설정을 변경해야 한다.
-- 1) 기존에 열린 퀴리 창을 모두 종료한다.
-- 2) EDIT-Preference 메뉴를 실행한다.
-- 3) Workbench Preference 창의 SQL Editor에서 Safe Updates (rejects UPDATEs and DELTEs with restrictions)를 체크 해제한 후 OK 버튼을 클릭한다.

USE market_db;
UPDATE city_popul
	SET city_name = '서울'
    WHERE city_name = 'Seoul';
SELECT * FROM city_popul WHERE city_name = '서울';

UPDATE city_popul
	SET city_name = '뉴욕', population = 0
    WHERE city_name = 'New York';
SELECT * FROM city_popul WHERE city_name = '뉴욕';

-- WHERE가 없는 UPDATE 문
-- 문법상 WHERE 절은 생략이 가능하다. 하지만, 생략하면 테이블의 모든 행의 값이 변경된다.
UPDATE city_popul
	SET population = population / 10000;
SELECT * FROM city_popul LIMIT 5;

-- DELETE 
-- DELETE는 행 단위로 삭제한다.
DELETE FROM city_popul
	WHERE city_name LIKE 'New%'; -- 도시 이름 앞에 New가 들어가는 도시 삭제
-- WHERE 절을 생략할 수 있지만, 생략되면 전체 행 데이터를 삭제한다.

DELETE FROM city_popul
	WHERE city_name 
    LIKE 'New%'
    LIMIT 5; -- New로 시작하는 도시 중 상위 5건만 삭제하는 경우