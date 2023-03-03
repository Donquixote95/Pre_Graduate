#GUI : Graphical User Interface

#tkinter는 파이썬에서 GUI 관련 모듈을 제공해주는 표준 윈도 라이브러리이다. 윈도 화면이 필요할 때는 꼭 써야 한다.
from tkinter import *

# Tk()는 기본이 되는 윈도를 반환한다. 이를 root라는 변수에 넣었다.
# Tk()를 root window(루트 윈도)라고도 부르며, 꼭 필요한 요소다. 이 행이 실행될 때 윈도가 출력된다.
root = Tk()

root.title("GUI 연습") #윈도에 제목을 표시한다.
root.geometry("600x400") #윈도 초기 크기를 400x200으로 지정한다.

# label(라벨)은 문자를 표현할 수 있는 위젯이다.
# Label(부모윈도, 옵션...) 형식을 사용한다
# widget(위젯)은 윈도에 나오는 버튼, 텍스트, 라디오 버튼, 이미지 등을 통합해서 지칭하는 용어다.
# 옵션에서 모양에 대한 다양한 설정을 할 수 있다. 모든 위젯들은 pack() 함수를 사용해야 화면에 나타난다.
label1 = Label(root, text = "SQL is") #부모윈도는 루트 윈도를 지정한 경우
label2 = Label(root, text = "really easy to understand.",
               font = ("궁서체", 15), bg = "blue", fg="yellow") #fg: foreground 글자색, bg: background 배경색

label1.pack() 
label2.pack()

# button(버튼)은 마우스로 클릭하면 지정한 작업이 실행되도록 사용하는 위젯이다.
# Button(부모윈도, 옵션...) 형식을 사용한다.
# command 옵션으로 사용자가 버튼을 눌렀을 때 지정한 작업을 처리해야 한다는 점이 라벨과 다르다.
from tkinter import messagebox # 메시지 상자를 사용하기 위해서 import
def clickButton() :
    messagebox.showinfo('버튼 클릭', '버튼을 눌렀습니다.')

button1 = Button(root, text = "Click Here",
                 fg = "red", bg = "yellow",
                 command=clickButton) #command 옵션에 clickButton() 함수를 call했다. 
button1.pack(expand = 1) #expand=1 옵션은 버튼을 화면 중앙에 표시하는 역할이다.

# 위젯의 정렬
# pack() 함수의 옵션 중에서 정렬하는 방법 side = Left or Right or Top or Bottom
button2 = Button(root, text = "Study2")
button3 = Button(root, text = "Study3")
button4 = Button(root, text = "Study4")
button5 = Button(root, text = "Study5")
button6 = Button(root, text = "Study6")

button2.pack(side=LEFT)
button3.pack(side=LEFT)

button4.pack(side=RIGHT)

button5.pack(side=TOP)
button6.pack(side=BOTTOM)

# 위젯 사이에 여백 추가
# pack() 함수의 옵션 중 padx=픽셀값 또는 pady=픽셀값 방식
# 위젯 사이에 여백이 생기면 화면이 좀 더 여유 있게 보인다.
button7 = Button(root, text = "Space7")
button8 = Button(root, text = "Space8")
button9 = Button(root, text = "Space9")

button7.pack(side=TOP, fill=X, padx=10, pady=10)
button8.pack(side=TOP, fill=X, padx=10, pady=10)
button9.pack(side=TOP, fill=X, padx=10, pady=10)

# frame(프레임)은 화면을 여러 구역으로 나눌 때 사용한다.
# entry(엔트리)는 입력 상자를 표현한다.
# listbox(리스트박스)는 목록을 표현한다.
upFrame = Frame(root) #Frame 2개를 생성, 구역을 나눴을 뿐 화면에 표시되진 않는다.
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width = 10) #입력을 위한 엔트리, upFrame에 나오게 했다.
editBox.pack(padx = 20, pady = 20)

listbox = Listbox(downFrame, bg = 'yellow') #리스트 박스는 downFrame에 나오게 했다.
listbox.pack()

listbox.insert(END, "One") #리스트 박스에 데이터를 3건 입력했다.
listbox.insert(END, "Two") #END 옵션은 데이터를 제일 뒤에 첨부하라는 의미이다. 그래서 차례대로 하나, 둘, 셋이 리스트 박스에 나온다.
listbox.insert(END, "Three")

#root.mainloop() 함수는 앞으로 윈도에 키보드 누르기, 마우스 클릭 등의 다양한 작업이 일어날 때 이벤트를 처리하기 위해 필요하다.
root.mainloop()