USE market_db;
SELECT * FROM member;
-- 테이블 전체 이름은 데이터베이스_이름.테이블_이름 형식으로 표현한다.
-- USE 문으로 지정해 놓은 데이터베이스가 있기 때문에 다음 문장과 동일하다.
-- SELECT * FROM market_db.member;

-- we could use column name as alias(별칭). we should group alias by " if there exists a white space.
SELECT addr 주소, debut_date "데뷔 일자", mem_name FROM member;

SELECT * FROM member WHERE mem_name = '블랙핑크';
SELECT * FROM member WHERE mem_number = 4;
SELECT mem_id, mem_name
	FROM member
    WHERE height <= 162;
    
SELECT mem_name, height, mem_number
		FROM member
        WHERE height >= 165 AND mem_number > 6;
        
SELECT mem_name, height, mem_number
	FROM member
    WHERE height >= 165 OR mem_number > 6;
    
SELECT mem_name, height
	FROM member
    WHERE height >= 163 AND height <= 165;
    
SELECT mem_name, height
	FROM member
    WHERE height BETWEEN 163 AND 165;
    
SELECT mem_name, addr
	FROM member
    WHERE addr = '경기' OR addr = '전남' OR addr = '경남';
    
SELECT mem_name, addr
	FROM member
    WHERE addr IN('경기', '전남', '경남');
    
SELECT *
	FROM member
    WHERE mem_name LIKE '우%'; -- %는 그 뒤에 무엇이든 허용한다는 뜻이다. LIKE는 문자열의 일부 글자를 검색하는데 사용한다.
    
-- 한 글자와 매치하기 위해서는 underbar(_)를 사용한다.
SELECT *
	FROM member
    WHERE mem_name LIKE '__핑크'; -- 앞의 두 글자는 상관없고 뒤는 핑크인 자료를 검색
    
-- subquery(서브 퀴리) 또는 하위 퀴리
SELECT mem_name, height 
	FROM member WHERE height > (SELECT height FROM member WHERE mem_name = '에이핑크');