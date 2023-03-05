-- 	INSERT 문에서 테이블 이름 다음에 나오는 열은 생략 가능하다. 생략한 경우 VALUES 다음에 나오는 값들의 순서 및 개수는 테이블을 정의할 때의 열 순서 및 개수와 동일해야 한다.

USE market_db;
CREATE TABLE practice (toy_id INT, toy_name CHAR(4), age INT);
INSERT INTO practice VALUES (1, '우디', 25);

INSERT INTO practice (toy_id, toy_name) VALUES (2, '버즈'); -- age를 생략하면 age 열에는 NULL 값이 들어간다.

INSERT INTO practice (toy_name, age, toy_id) VALUES ('제시', 20, 3); -- 순서를 바꿔서 입력할 수도 있다.

SELECT * FROM market_db.practice