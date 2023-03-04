-- ORDER BY 절은 결과의 값이나 개수에 대해서는 영향을 미치지 않는다. 결과가 출력되는 순서를 조절한다.

USE market_db;

SELECT mem_id, mem_name, debut_date, height
	FROM member
    WHERE height >= 164
    ORDER BY height DESC, debut_date ASC; -- 기본값은 ASC(Ascending)이다. 즉, 오름차순이다. 생략하면 ASC로 인식한다.
										  -- DESC(descending), 내림차순을 의미한다.
                                          
-- LIMIT 출력하는 개수를 제한한다. 형식은 다음과 같다. LIMIT 시작, 개수 // 첫 데이터는 0번째
-- LIMIT 개수 OFFSET 시작 이라는 형식과 동일하다.
SELECT *
	FROM member
    ORDER BY debut_date
    LIMIT 2 OFFSET 3;
    -- 위와 동일하다. LIMIT 3, 2; -- 3번째부터 2건 조회
    
-- DISTINCT 중복된 결과 제거 // 조회된 결과에서 중복된 데이터를 1개만 남긴다.
SELECT DISTINCT addr FROM member;

-- GROUP BY 그룹으로 묶어주는 역할을 한다.
-- 집계 함수는 주로 GROUP BY 절과 함께 쓰이며 데이터를 grouping 하는 기능을 한다.
-- 집계함수는 SUM(), AVG(), MIN(), MAX(), COUNT() 등이 있다.
-- COUNT() 함수는 행의 개수를 센다. COUNT(DISTINCT) 행의 개수를 세지만, 중복을 1개만 인정한다.
SELECT mem_id "회원 아이디", SUM(amount) "총 구매 개수", SUM(price * amount) "총 구매 금액", AVG(amount) "평균 구매 개수"
	FROM buy 
    GROUP BY mem_id;
    
-- COUNT()
SELECT COUNT(phone1) FROM member; -- NULL 값은 제외하고 count된다.

-- Having 절
SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
	FROM buy
    GROUP BY mem_id
    HAVING SUM(price*amount) > 1000 -- HAVING 절은 GROUP BY 절 다음에 나와야 하고, 집계함수에 관한 조건을 제한한다.(WHERE는 불가)
    ORDER BY SUM(price*amount) DESC;
    