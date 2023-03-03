#GUI 화면에서 데이터의 입력과 수정, 초기화 버튼을 클릭하면 테이블이 삭제되고 재생성되도록 작성
#다음 두 작업은 선행되었다고 가정한다.
# MySQL에서 워크벤치를 실행
# (1) DROP DATABASE IF EXISTS soloDB;
# (2) CREATE DATABASE soloDB;

#참고, ;(semi colon)은 줄을 분리해주는 효과

import pymysql
from tkinter import *
from tkinter import messagebox

# Main Code

# Initailize
def insertData() :
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""

# Connect
    conn = pymysql.connect(
                            host = '127.0.0.1',
                            user = 'root',
                            port = 3306, #안 입력해도 실행 가능
                            password = '****', #원래 비밀번호 입력
                            db = 'soloDB',
                            charset = 'utf8'
                            )
# Create Cursor    
    cur = conn.cursor()

# Insert Data
    data1 = edt1.get(); data2 = edt2.get() #화면의 4개의 entry에서 값을 가져온다.
    data3 = edt3.get(); data4 = edt4.get()
    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")" #퀴리문을 만들어서 실행한다.
        #data1~3는 작은따옴표(')로 묶어야 하고, data4는 정수이므로 작은따옴표로 묶으면 안 된다.

# Execute
    cur.execute(sql)

# Commit
    conn.commit()

# Close
    conn.close()

    messagebox.showinfo('success', 'input data success') #입력이 성공한 것을 메시지 상자로 표시한다.


def selectData() :
    # Initailize
    strData1, strData2, strData3, strData4 = [], [], [], [] #사용자 ID열의 결과를 리스트 박스에 출력하기 위한 리스트
    # Connect
    conn = pymysql.connect(
                            host = '127.0.0.1',
                            user = 'root',
                            password = '8656',
                            db = 'soloDB',
                            charset = 'utf8'
                            )
    # Create Cursor    
    cur = conn.cursor()
    # Searching
    cur.execute("SELECT * FROM userTable")

    # Store Data
    strData1.append("User ID");         strData2.append("User Name")
    strData3.append("User E-mail");     strData4.append("User Birthday")
    strData1.append("----------");      strData2.append("----------") #제목 및 구분하기 위한 줄을 리스트에 추가
    strData3.append("----------");      strData4.append("----------")

    while (True) :
        row = cur.fetchone() #call by row by row
        #fetchone()함수로 조회된 결과가 row 변수에 저장된다. row 변수는 튜플(Tuple) 형식으로 각 행 데이터가 저장되어 있다.
        if row == None : #if there is no data, exit the while loop
            break
        strData1.append(row[0]);    strData2.append(row[1]) #리스트에 사용자 ID를 하나씩 추가했다.
        strData3.append(row[2]);    strData4.append(row[3]) #결국 strData1 에는 "사용자 ID", "사용자"ID, ... 형식의 모든 사용자 ID가 저장된다.

    listData1.delete(0,listData1.size() - 1) # 일단 화면에서 4개의 리스트 박스를 모두 비운다.
    listData2.delete(0,listData1.size() - 1)
    listData3.delete(0,listData1.size() - 1)
    listData4.delete(0,listData1.size() - 1)

    for item1, item2, item3, item4 in zip( #동시에 여러 개의 리스트 항목에 접근하기 위해 zip() 함수 사용
        strData1, strData2, strData3, strData4):
        listData1.insert(END, item1);   listData2.insert(END, item2) #END옵션은 끝에 추가하라는 뜻
        listData3.insert(END, item3);   listData4.insert(END, item4) #각 리스트 박스에 앞에서 준비한 strData1~4값들을 다시 채운다. 
        #결국 화면의 리스트 박스에는 조회된 결과가 모두 출력된다.
    
    # Close
    conn.close()

# Main code

# Tk()는 기본이 되는 윈도를 반환한다. 이를 root라는 변수에 넣었다.
# Tk()를 root window(루트 윈도)라고도 부르며, 꼭 필요한 요소다. 이 행이 실행될 때 윈도가 출력된다.
root = Tk()
#윈도 초기 크기를 600x300으로 지정한다.
root.geometry("600x300")
#윈도에 제목을 표시한다.
root.title("Perfect GUI application program")

# frame(프레임)은 화면을 여러 구역으로 나눌 때 사용한다.
edtFrame = Frame(root)
# 모든 위젯들은 pack() 함수를 사용해야 화면에 나타난다.
edtFrame.pack()

listFrame = Frame(root)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1) #expand=1 옵션은 화면 중앙에, side bottom은 정렬 기준을 의미한다.

# entry(엔트리)는 입력 상자를 표현한다.
# pack() 함수의 옵션 중 padx=픽셀값 또는 pady=픽셀값 방식
edt1 = Entry(edtFrame, width=10);   edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10);   edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10);   edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10);   edt4.pack(side=LEFT, padx=10, pady=10)

# button(버튼)은 마우스로 클릭하면 지정한 작업이 실행되도록 사용하는 위젯이다.
btnInsert = Button(edtFrame, text = "Input", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)

btnSelect = Button(edtFrame, text = "search", command = selectData)
btnSelect.pack(side=LEFT, padx = 10, pady = 10)

# listbox(리스트박스)는 목록을 표현한다.
listData1 = Listbox(listFrame, bg = 'yellow')
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg = 'yellow')
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg = 'yellow')
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg = 'yellow')
listData4.pack(side=LEFT, fill=BOTH, expand=1)


#root.mainloop() 함수는 윈도에 키보드 누르기, 마우스 클릭 등의 다양한 작업이 일어날 때 이벤트를 처리하기 위해 필요하다.
root.mainloop()