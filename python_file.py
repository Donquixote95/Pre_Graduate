"""
파이썬 표준 함수에는 파일과 관련된 처리를 함수가 기본으로 제공된다.
파일은 크게 
 1) 텍스트 파일
 2) 바이너리 파일
로 구분된다. 텍스트 파일을 먼저 다뤄보자.

파일을 처리하려면 일단 파일 열기open을 해야 한다. 파일을 열면 파일 읽기read 또는 파일 쓰기write를 할 수 있다.
"""

# 파일 열고 닫기 ; open() 함수 사용
"""
파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)
"""
# open() 함수의 첫 번째 매개변수에는 파일 경로path를 입력하고, 두 번째 매개변수에는 모드mode를 지정한다.
"""
모드에는 다음과 같은 것을 지정할 수 있다.
w ; wirte 모드(새로 쓰기 모드)
a ; append 모드(뒤에 이어서 쓰기 모드)
r ; read 모드(읽기 모드)
"""

# 파일을 닫을 때는 close() 함수를 사용한다
"""
파일 객체.close()
"""

# 파일을 연다
file = open("basic.txt", "w")

# 파일에 텍스트를 쓴다.
file.write("Hello Python Programming!")

# 파일을 닫는다.
file.close()

# with 키워드 ; with 구문이 종료될 때 자동으로 파일이 닫힌다. 실수 방지
"""
with open(문자열: 파일 경로, 문자열: 모드) as 파일 객체:
    문장
"""

# 파일을 연다
with open("basic.txt", "w") as file:
    # 파일에 텍스트를 쓴다.
    file.write("Nice to see you.")


# stream(스트림)
"""
프로그램이 외부 파일, 외부 네트워크 등과 통신할 때 데이터가 흐르는 길.
open() 함수는 프로그램에서 파일로 흐르는 길을 만드는 것
close() 함수는 프로그램에서 파일로 흐르는 길을 닫는 것

with 키워드는 이러한 스트림을 열고 닫는 실수를 줄이고자 만들어진 구문이다.
네트워크로 흐르는 길을 열고 닫을 때도 사용한다.
"""

# read() 함수 ; 텍스트 읽기
"""
파일 객체.read()

파일을 열고 파일 객체의 read() 함수를 호출하기만 하면 내부에 있는 데이터를 모두 읽어 출력한다.
"""
# read() 함수로 텍스트 읽기
# 파일을 연다
with open("basic.txt", "r") as file:
    # 파일을 읽고 출력
    contents = file.read()
print(contents)

# 텍스트 한 줄씩 읽기
"""
텍스트를 사용해 데이터를 구조적으로 표현할 수 있는 방법 ; CSV, XML, JSON
CSV ; Comma Separated Values ; 쉼표로 구분된 값
csv 파일은 첫 번째 줄에 header(헤더)를 넣고 아래 데이터를 넣는다. 데이터는 쉼표를 사용해서 구분한다.

이름, 키, 몸무게 #header
라일락, 185, 74 #data
그리미, 170, 65
"""

# 랜덤하게 1000명의 키와 몸무게 만들기
# 랜덤한 숫자를 만들기 위해 가져온다.
import random
# 간단한 한글 리스트를 만든다.
hanguls = list("가나다라마바사아자차카타파하")
# 파일을 쓰기 모드로 연다
with open("info.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성한다.
        name = random.choice(hanguls) + random.choice(hanguls)
        name = name.encode('utf-8')
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트를 쓴다.
        file.write("{}, {}, {}\n".format(name, weight, height))

# 데이터가 많이 있다고 가정하고 한 줄씩 읽기
# 데이터를 한 줄씩 읽어 들일 때는 for반복문을 다음과 같은 형태로 사용

"""
for 한 줄을 나타내는 문자열 in 파일 객체:
    처리
"""

# 반복문으로 파일 한 줄씩 읽기
with open("info.txt", "r") as file:
    for line in file:
        # 변수 선언
        (name, weight, height) = line.strip().split(",")

        # 데이터가 문제가 없는지 확인 : 문제가 있으면 지나감
        if (not name) or (not weight) or (not height):
            continue
        # 결과를 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = '과체중'
        elif 18.5 <= bmi:
            result = '정상 체중'
        else:
            result = '저체중'
        
        # 출력
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name,weight,height,bmi,result))
        print()