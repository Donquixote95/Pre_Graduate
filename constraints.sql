use naver_db;
drop table if exists buy, member;
create table member
(mem_id char(8) not null primary key,
mem_name varchar(10) not null,
height tinyint unsigned null
);

CREATE table buy
(num int auto_increment not null primary key,
mem_id char(8) not null,
prod_name char(6) not null,
foreign key(mem_id) references member(mem_id)
);

-- 기본 키-외래 키 관계로 연결된 테이블은 외래 키가 설정된 테이블을 먼저 삭제해야 한다.
-- 참조 테이블이 참조하는 기준 테이블의 열은 반드시 PK 또는 UK(Unique Key)로 설정되어 있어야 한다.

-- 외래 키 형식
-- FOREIGN KEY(Column Name) REFERENCES 기준_테이블(열_이름)

-- alter table에서 설정하는 외래 키 제약조건
drop table if exists buy;
CREATE table buy
(num int auto_increment not null primary key,
mem_id char(8) not null,
prod_name char(6) not null
);
ALTER table buy
	add constraint
    foreign key(mem_id)
    references member(mem_id);
    
INSERT INTO member values('BLK', '블랙핑크', 163);
INSERT INTO buy VALUES(NULL, 'BLK', '지갑');
INSERT INTO buy VALUES(NULL, 'BLK', '맥북');

SELECT M.mem_id, M.mem_name, B.prod_name
	FROM buy B
		inner join member M
        ON B.mem_id = M.mem_id;
        
UPDATE member SET mem_id = 'PINK' WHERE mem_id = 'BLK';
DELETE FROM member WHERE mem_id = 'BLK';

-- ON UPDATE CASCADE, ON DELETE CASCADE 문은 기준 테이블의 데이터가 변경되면 참조 테이블의 데이터도 변경되는 기능이다.
drop table if exists buy;
CREATE table buy
(num int auto_increment not null primary key,
mem_id char(8) not null,
prod_name char(6) not null
);
ALTER table buy
	add constraint
    foreign key(mem_id) references member(mem_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE;
INSERT INTO buy VALUES(NULL, 'BLK', '지갑');
INSERT INTO buy VALUES(NULL, 'BLK', '맥북');    
UPDATE member SET mem_id = 'PINK' WHERE mem_id = 'BLK';

SELECT M.mem_id, M.mem_name, B.prod_name
	FROM buy B
		INNER JOIN member M
        ON B.mem_id = M.mem_id;
DELETE FROM member WHERE mem_id = 'PINK';
SELECT * FROM buy;

-- 고유 키 제약조건(Unique 제약조건) ; '중복되지 않는 유일한 값'을 입력해야 하는 조건, NULL 값도 허용한다. 고유 키는 여러 개 설정해도 된다.
DROP table if exists buy, member;
create table member
(mem_id char(8) not null primary key,
mem_name varchar(10) not null,
height tinyint unsigned null,
email char(30) null unique -- 고유 키를 설정할 열을 NOT NULL로 지정하면 기본 키와 동일하게 중복도 안 되고 비어 있어도 안 된다.
);

INSERT INTO member values('BLK', '블랙핑크', 163, 'pink@gmail.com');
INSERT INTO member values('TWC', '트와이스', 167, NULL);
INSERT INTO member values('APN', '에이핑크', 164, 'pink@gmail.com'); -- 중복이라서 되지 않는다.

-- 체크 제약조건
-- CHECK 제약조건은 입력되는 데이터를 점검하는 기능을 한다. 

DROP table if exists member;
create table member
(mem_id char(8) not null primary key,
mem_name varchar(10) not null,
height tinyint unsigned null CHECK (height >= 100),
phone1 char(3) NULL
);

INSERT INTO member values('BLK', '블랙핑크', 163, NULL);
INSERT INTO member values('TWC', '트와이스', 99, NULL);

-- 테이블을 만든 후에 alter table 문으로 제약조건을 추가할 수 있다.
alter table member
	add constraint
    check (phone1 IN ('02', '031', '032', '054', '055', '061')); -- IN()은 괄호 안에 있는 값 중 하나와 같아야 참이 된다.
    
INSERT INTO member values('TEST', '테스트', 163, '02');
INSERT INTO member values('OMY', '오마이걸', 167, '010');

-- 기본값 정의(Default) ; 값을 입력하지 않았을 때 자동으로 입력될 값을 미리 지정해 놓는 방법
DROP table if exists member;
create table member
(mem_id char(8) not null primary key,
mem_name varchar(10) not null,
height tinyint unsigned null CHECK (height >= 100) default 160,
phone1 char(3) NULL
);

alter table member
	alter column phone1 set default '02';
    
insert into member values('RED', '레드벨벳', 161, '054');
insert into member values('SPC', '우주소녀', default, default);
SELECT * FROM member;