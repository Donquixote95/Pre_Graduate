#Step 1. MySQL에 연결하기
import pymysql
conn = pymysql.connect(
                        host = '127.0.0.1', 
                        port = 3306,
                        user = 'root', 
                        password = '8656', 
                        db = 'soloDB', 
                        charset = 'utf8') 
 #utf8을 사용하는 이유는 한글을 사용하기 위해서이다.
 #모듈을 임포트하고 데이터베이스와 연동해야 한다.

#Step 2. Create Cursor
cur = conn.cursor()
 #커서는 데이터베이스에 SQL문을 실행하거나 실행된 결과를 돌려받는 통로
 #앞 단계에서 연결한 연결자에 커서를 만들어야 한다.

#Step 3. Create Table 
cur.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)")
 #테이블을 만드는 SQL 문을 커서이름.execute() 함수의 매개변수로 넘겨주면 SQL 문이 데이터베이스에 실행된다.
 #즉, 파이썬에서도 MySQL 워크벤치에서 사용한 것과 동일한 SQL 문을 사용하면 된다.

#Step 4. Input data
cur.execute("INSERT INTO userTable VALUES('hong', '홍지윤','hong@naver.com', 1996)")
cur.execute("INSERT INTO userTable VALUES('kim', '김태연','kim@daum.net', 2011)")
cur.execute("INSERT INTO userTable VALUES('star', '별사랑','star@nparan.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('yang', '양지은','yang@gmail.com', 1993)")

#Step 5. Store the input data
conn.commit()

#Stpe 6. Close connect with MySQL
conn.close()