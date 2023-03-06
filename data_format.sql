-- data format

-- 정수형
-- tinyint 	1byte -128 ~ 127
-- smallint 2byte -32.768 ~ 32.767
-- int 		4byte 약 -21억 ~ 21억
-- bigint	8byte 약 -900경 ~ 900경

-- UNSIGNED 예약어를 사용하면, -범위를 제하고, N+{0} 에서 사용할 수 있다.
-- TINY UNSIGNED	1byte	0 ~ 255

USE market_db;
CREATE TABLE practice4 (
	tinyint_col  TINYINT,
    smallint_col SMALLINT,
    int_col 	 INT,
    bigint_col	 BIGINT );

INSERT INTO practice4 VALUES(127, 32767, 2147483647, 90000000000000);

INSERT INTO practice4 VALUES(1270, 327670, 21474836470, 900000000000000000000);

DROP TABLE Practice4;

-- 문자형
-- CHAR		1~255byte		고정길이 문자형
-- VARCHAR	1~16383byte		가변길이 문자형

-- VARCHAR(10)에 'abc' 3글자만 저장할 경우 3자리만 사용한다.
-- CHAR(10)에 'abc' 3글자만 저장해도 10자리를 모두 사용한다. 7자리는 낭비된다.

-- memory efficiency는 VARCHAR가 char보다 좋다.
-- time efficiency(빠른 속도)는 CHAR가 VARCHAR보다 빠르다.

-- 데이터가 숫자라도 다음 두 가지 중 하나에 해당하지 않는다면 문자형으로 저장하는 것을 고려해야 한다.
 -- 1) 숫자의 연산(더하기, 빼기 등)을 할 필요가 있다.
 -- 2) 대소 관계 혹은 순서를 고려해야 할 일이 있다.
 -- 이외, 데이터 형식이 정수형일 때 숫자 0이 맨 앞에 있는 데이터는 0이 사라진다. 대표적으로 031과 같은 지역번호 데이터는 문자형으로 지정해야 한다.
 
 
 -- 대량의 데이터 형식
 
 -- TEXT 형식 ; 소설, 영화 대본과 같은 내용을 저장할 때 사용하는 데이터 형식
 -- TEXT		1~65535 byte
 -- LONGTEXT	1~4294967295 byte
 
 -- BLOB 형식 ; Binary Long Object의 약자로 이미지, 동영상 등의 데이터이다. Binary Data
 -- BLOB		1~65535 byte
 -- LONGBLOB	1~4294967295 byte
 
 CREATE DATABASE netflix_db;
 USE netflix_db;
 CREATE TABLE movie
	(movie_id		INT,
	 movie_title	VARCHAR(30),
     movie_director VARCHAR(20),
     movie_star		VARCHAR(20),
     movie_script	LONGTEXT,
     movie_film		LONGBLOB
     );
     
DROP DATABASE netflix_db;

-- 실수형
-- FLOAT	4byte	소수점 아래 7자리까지 표현
-- DOUBLE	8byte	소수점 아래 15자리까지 표현

-- 날짜형
-- DATE			3byte	날짜만 저장. YYYY-MM-DD 형식으로 사용
-- TIME			3byte	시간만 저장. HH:MM:SS 형식으로 사용
-- DATETIME		8byte	날짜 및 시간을 저장. YYYY-MM-DD HH:MM:SS 형식으로 사용
-- 저장할 때는 작은따옴표로 묶어줘야 한다. (문자도 마찬가지)