-- 스토어드 프로시저

-- 기본 구조
-- DELIMITER $$
-- CREATE PROCEDURE 스토어드_프로시저_이름()
-- BEGIN
	-- SQL 프로그래밍 코딩
-- END $$
-- DELIMITER ;
-- CALL 스토어드_프로시저_이름();
-- 구분 문자(DELMITER)는 $$를 많이 사용하지만, 원한다면 /, &, @ 등을 사용해도 좋다. 다른 기호와 중복될 수 있으므로 기호 2개를 연속해서 사용하는 것을 권장

-- IF문
-- 기본 구조
-- IF <cndition> THEN
	-- SQL
-- END IF;

-- 위에서 SQL 문이 한 문장이면 그 문장만 써도 되지만, 두 문장 이상이면 BEGIN~END로 묶어줘야 한다.

-- SQL에서 같다는 '='이다. 다른 프로그래밍 언어는 대부분 '=='을 사용하는 것과 대비되는 점이다.
-- SELECT 뒤에 문자가 나오면 다른 언어의 print() 함수와 유사한 기능을 수행한다.
USE market_db;
DROP PROCEDURE IF EXISTS ifProc3;
DELIMITER $$
CREATE PROCEDURE ifProc3()
BEGIN
	DECLARE debutDate DATE;
    DECLARE curDate DATE;
    DECLARE days INT;
    
    SELECT debut_date INTO debutDate -- SELECT와 함께 INTO가 붙으면 결과를 변수에 저장한다.
		FROM market_db.member
        WHERE mem_id = 'APN';
        
	SET curDATE = CURRENT_DATE(); -- 현재 날짜
    SET days = DATEDIFF(curDATE, debutDate); -- 날짜의 차이, 일 단위
    
    IF (days/365) >= 5 THEN
		SELECT CONCAT('데뷔한 지', days, '일이 지났습니다.');
	ELSE
		SELECT '데뷔한 지' + days + '일 되었네요. 화이팅!';
	END IF;
END $$
DELIMITER ;
CALL ifProc3();

-- 날짜와 관련된 함수
-- CURRENT_DATE(); 오늘 날짜를 알려준다.
-- CURRENT_TIMESTAMP(); 오늘 날짜 및 시간을 함께 알려준다.
-- DATEDIFF(날짜1, 날짜2); 날짜2부터 날짜1까지 일수를 알려준다.
SELECT CURRENT_DATE(), DATEDIFF('2022-12-31', '2023-12-31');

-- CASE 문
-- 다중 분기, 다른 프로그래밍 언어의 SWITCH ~ CASE 문과 비슷한 기능을 한다.
DROP PROCEDURE IF EXISTS caseProc;
DELIMITER $$
CREATE PROCEDURE caseProc()
BEGIN
	DECLARE point INT;
    DECLARE credit CHAR(1);
    SET point = 88;
    
    CASE
	 WHEN point >= 90 THEN
		SET credit = 'A';
	 WHEN point >= 80 THEN
		SET credit = 'B';
	 WHEN point >= 70 THEN
		SET credit = 'C';
	 WHEN point >= 60 THEN
		SET credit = 'D';
	 ELSE
		SET credit = 'F';
	END CASE;
    SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;
CALL caseProc();

-- CASE 문 활용
SELECT mem_id, SUM(price*amount) "총구매액"
	FROM buy
    GROUP BY mem_id
    ORDER BY SUM(price * amount) DESC;
    
SELECT B.mem_id, M.mem_name,
		SUM(price*amount) "총구매액"
	FROM buy B
		INNER JOIN member M
        ON B.mem_id = M.mem_id
	GROUP BY B.mem_id
    ORDER BY SUM(price * amount) DESC;
    
SELECT M.mem_id, M.mem_name, SUM(price*amount) "총구매액",
	 CASE
		 WHEN (SUM(price*amount) >= 1500) THEN '최우수고객'
		 WHEN (SUM(price*amount) >= 1000) THEN '우수고객'
		 WHEN (SUM(price*amount) >= 1) THEN '일반고객'
		 ELSE '유령고객'
	 END "회원등급"
	FROM buy B
		RIGHT OUTER JOIN member M
        ON B.mem_id = M.mem_id
	GROUP BY M.mem_id
    ORDER BY SUM(price * amount) DESC;
    
-- CASE
-- WHEN (총 구매액 >= 1500) THEN '최우수고객'
-- WHEN (총 구매액 >= 1000) THEN '우수고객'
-- WHEN (총 구매액 >= 1) THEN '일반고객'
-- ELSE '유령고객'
-- END

-- WHILE문
DROP PROCEDURE IF EXISTS whileProc;
DELIMITER $$
CREATE PROCEDURE whileProc()
BEGIN
	DECLARE i INT; -- 1에서 100까지 증가할 변수
    DECLARE hap INT; -- 더한 값을 누적할 변수
    SET i = 1;
    SET hap = 0;
    
    WHILE (i <= 100) DO
		SET hap = hap + i;
        SET i = i +1;
	END WHILE;
    
    SELECT '1부터 100까지의 합 ==>', hap;
END $$
DELIMITER ;
CALL whileProc();

-- while 문의 응용
-- ITERATE [레이블] : 지정한 레이블로 가서 계속 진행 // 다른 프로그래밍 언어의 CONTINUE와 비슷하다. 
-- LEAVE [레이블] : 지정한 레이블을 빠져나간다. while 문이 종료된다. // 다른 프로그래밍 언어의 BREAK와 비슷하다.
DROP PROCEDURE IF EXISTS whileProc2;
DELIMITER $$
CREATE PROCEDURE whileProc2()
BEGIN
	DECLARE i INT; 
    DECLARE hap INT;
    SET i = 1;
    SET hap = 0;
    
    myWhile: -- while문을 myWhile이라는 레이블로 지정
    WHILE (i <= 100) DO
		IF (i%4 = 0) THEN
			SET i = i + 1;
            ITERATE myWhile; -- 지정한 label 문으로 가서 계속 진행
		END IF;
        SET hap = hap + i;
        IF (hap > 1000) THEN
			LEAVE myWhile; -- 지정한 label 문을 떠남. 즉 While 종료
		END IF;
        SET i = i + 1;
        END WHILE;
        
        SELECT '1부터 100까지의 합(4의 배수 제외), 1000 넘으면 종료 ==>', hap;
END $$
DELIMITER ;
CALL whileProc2();

-- 동적 SQL
-- PREPARE, EXECUTE 이후에는 DEALLOCATE PREPARE로 문장을 해제해주는 것이 바람직하다.
use market_db;
PREPARE myQuery FROM 'SELECT * FROM member WHERE mem_id = "BLK"';
EXECUTE myQuery;
DEALLOCATE PREPARE myQuery;

-- 동적 SQL의 활용
-- PREPARE 문에서 ?로 향후에 입력될 값을 비워 놓고
-- EXECUTE에서 USING으로 ?에 값을 전달할 수 있다.
DROP TABLE IF EXISTS gate_table;
CREATE TABLE gate_table (id INT AUTO_INCREMENT PRIMARY KEY, entry_time
	DATETIME);

SET @curDate = CURRENT_TIMESTAMP(); -- 현재 날짜와 시간

PREPARE myQuery FROM 'INSERT INTO gate_table VALUES(NULL, ?)';
EXECUTE myQuery USING @curDate;
DEALLOCATE PREPARE myQuery;

SELECT * FROM gate_table;