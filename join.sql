-- join 

-- 내부조인(inner join), 조인이라고 함은 보통 내부 조인을 의미한다.
-- 테이블이 one to many(일대다) 관계로 연결되어야 한다.

-- 관계, relation, 테이블은 관계를 맺고 있다.

-- 일대다 관계란 한쪽 테이블에는 하나의 값만 존재하지만, 연결된 다른 테이블에는 여러 개의 값이 존재할 수 있는 관계다.
-- Primary Key, 기본 키, PK
-- Foreing Key, 외래 키, FK

-- 두 테이블의 조인을 위해서는 기본 키 - 외래 키 관계로 맺어져야 하고, 이를 일대다 관계라고 부른다.

-- 상호 조인은 기본 키- 외래 키 관계가 아니어도 가능한 조인이다. 이외는 위 관계가 핵심이다.

-- 조인은 3개 이상의 테이블도 가능하다. 보통 2개를 한다.

USE market_db;
SELECT *
	FROM buy
    INNER JOIN member
    ON buy.mem_id = member.mem_id;
	-- WHERE buy.mem_id = 'GRL';
    
SELECT B.mem_id, M.mem_name, B.prod_name, M.addr, 
		CONCAT(M.phone1, M.phone2) '연락처'
	FROM buy B -- alias
    INNER JOIN member M -- alias(별칭)
    ON B.mem_id = M.mem_id;
	-- WHERE buy.mem_id = 'GRL';

-- 내부 조인의 활용    
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
	FROM buy B
    INNER JOIN member M
    ON B.mem_id = M.mem_id
    ORDER BY M.mem_id;

-- 중복된 결과 1개만 출력하기
SELECT DISTINCT M.mem_id, M.mem_name, M.addr
		FROM buy B
        INNER JOIN member M
        ON B.mem_id = M.mem_id
		ORDER BY M.mem_id;
        
-- Outer join(외부 조인) 
-- 내부 조인은 두 테이블 모두 데이터가 있어야만 결과가 나오지만, 이와 달리 외부 조인은 한쪽에만 데이터가 있어도 결과가 나온다.

-- 전체 회원의 구매 기록 출력
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
	FROM member M
    LEFT OUTER JOIN buy B -- 왼쪽에 있는 회원 테이블을 기준으로 외부 조인
    ON M.mem_id = B.mem_id
    ORDER BY M.mem_id;