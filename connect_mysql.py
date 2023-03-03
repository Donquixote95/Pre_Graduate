#Step 1. MySQL에 연결하기
import pymysql
conn = pymysql.connect(
                        host = '127.0.0.1', 
                        port = 3306,
                        user = 'root', 
                        password = '****', #실제 비밀번호 입력
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


#%% 완전한 데이터 입력 프로그램 완성
#사용자가 반복해서 데이터를 입력하는 코드 작성

import pymysql

# global variable
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# Main code
# table이 윗 단계에서 생성되었다고 가정
conn = pymysql.connect(host = '127.0.0.1', 
                       user = 'root', 
                       password = '****', #실제 비밀번호 입력
                       db = 'soloDB',
                       charset = 'utf8')
cur = conn.cursor()

#반복하면서 data1~4를 입력받는다. data1에서 아무것도 입력하지 않고 Enter 키를 입력하면 while문을 빠져나간다.
while (True) :
    data1 = input("사용자 ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
    #data1~3는 작은따옴표(')로 묶어야 하고, data4는 정수이므로 작은따옴표로 묶으면 안 된다.

    #생성한 문자열을 실행해서 데이터를 입력한다.
    cur.execute(sql) 

conn.commit()
conn.close()

#%%
#MySQL의 데이터 조회를 위한 파이썬 코딩 순서

#1단계 : MySQL 연결
import pymysql
#global variable
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

conn = pymysql.connect(host = '127.0.0.1', 
                       user = 'root', 
                       password = '****', #실제 비밀번호 입력
                       db = 'soloDB',
                       charset = 'utf8')

#2단계 : 커서 생성
cur = conn.cursor()

#3단계 : 데이터 조회
#커서에 SELECT로 조회한 결과를 한꺼번에 저장해 둔다. 아래에서는 cur 변수에 저장했다.
cur.execute("SELECT * FROM userTable")

#4단계 : 조회한 데이터 출력
#조회한 데이터를 fetchone() 함수로 한 행씩 접근한 후 출력한다.
#조회하는 것은 데이터를 입력하거나 변경하는 것이 아니므로 commit(저장) 할 필요는 없다.
print("사용자ID         사용자이름          이메일          출생연도")
print("----------------------------------------------------------")

while (True) :
    row = cur.fetchone()
    if row == None : #조회한 결과가 없으면 초기화된 값인 None 값을 반환하여 while 문을 빠져나온다.
        break
    data1 = row[0] #fetchone()함수로 조회된 결과가 저장된 row 변수에는 튜플 형식으로 각 행 데이터가 저장된다.
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s    %15s    %20s    %d" % (data1, data2, data3, data4))

#5단계 : MySQL 연결 종료
conn.close()