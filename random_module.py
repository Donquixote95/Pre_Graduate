# random module ; random한 값을 생성할 때 사용하는 모듈

import random
print("# random module")

# random(): 0.0 <= 1.0 사이의 flaot를 리턴
print("- random():", random.random())

# uniform(min, max): 지정한 범위 사이의 float를 리턴
print("- uniform(10, 20):", random.uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴한다.
# - randrange(max): 0부터 max 사이의 값을 리턴한다.
# - randrange(min): min부터 max 사이의 값을 리턴한다.
print("- randrange(10):", random.randrange(10))

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택한다.
print("- choice([1, 2, 3, 4, 5]):", random.choice([1,2,3,4,5]))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞는다.
print("- shuufle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5]))

# sample(list, k=(숫자)): 리스트의 요소 중에 k개를 뽑는다.
print("- sample([1,2,3,4,5], k=2):", random.sample([1,2,3,4,5], k=2))


# module 이름과 같은 이름으로 파일을 저장하면 import할 떄 TypeError가 발생한다. 
# 왜냐하면, import 구문은 가장 먼저 현재 폴더에서 import 뒤에 적어 놓은 파일을 찾고, 찾으면 이를 모듈로 인식하고 읽어 들이기 때문이다.

from random import random, randrange, choice
# %%
# sys 모듈 ; 시스템과 관련된 정보를 가지고 있는 모듈. 명령 매개변수를 받을 때 많이 사용한다.
import sys
# 명령 매개변수를 출력
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력한다.
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램을 강제로 종료
sys.exit()
# %%
# os 모듈
import os
print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거(폴더가 비어있을 때만 제거 가능)
os.mkdir("hello2")
os.rmdir("hello2")

# 파일을 생성하고, 파일 이름을 변경
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거
os.remove("new.txt")
# os. unlink("new.txt"), unlink와 remove 함수는 같은 기능

# 시스템 명령어 실행
os.system("dir")

# %%
# datetime 모듈 ; date(날짜), time(시간)
import datetime
# 현재 시각을 구하고 출력
print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
print("----")

# 시간 출력 방법
print("# 시간을 포맷에 맞춰 출력")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()
# strftime() 함수를 사용하면 시간을 형식에 맞춰서 출력할 수 있다. 
# 다만 한국어 등의 문자는 매개변수로 넣을 수 없다. ouput_b, ouput_c 방법 활용

# %%
import datetime
now = datetime.datetime.now()

# 특정 시간 이후의 시간 구하기
print("#datetime.timedleta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1,\
        days=1,\
        hours=1,\
        minutes=1,\
        seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

# 특정 시간 요소 교체하기
print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year+1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

#timedleta(); 특정한 시간의 이전 또는 이후를 구할 수 있다. 다만 1년 후 등을 구하는 기능은 없다.
#relpace(); 1년 후를 구할 때 주로 사용한다. 날짜 값을 교체한다.
# %%
# time모듈 ; 시간과 관련된 기능을 다룰 수 있다.
# UNIX Time ; 1970년 1월 1일 0시 0분 0초를 기준으로 계산한 시간 단위
# 특정 시간 동안 코드 진행을 정지할 때 많이 사용한다.

import time
# time.sleep() ; 특정 시간 동안 코드 진행을 정지한다. 매개변수에 초 단위로 입력
print("지금부터 3초 동안 정지")
time.sleep(3)
print("프로그램 종료")
# %%
# urllib ; URL을 다루는 라이브러리, 인터넷 주소를 활용할 때 사용한다.
# URL ; Uniform Resource Locator ; 네트워크 자원(Resource)이 어디에 위치(locate)하는지 확인할 때 사용
from urllib import request

# urlopen() 함수로 구글의 메인 페이지 읽기
target = request.urlopen("https://google.com")
output = target.read()
# 출력
print(output)

# urlopen() ; URL 주소의 페이지를 열어준다. 파이썬이 해당 주소에 들어간다. 
# 이어서 read() ; 함수를 호출하면 해당 웹페이지에 있는 내용을 읽어서 가져온다.
# 실행 결과에 'b' 라는 글자가 붙어있는데 '바이너리 데이터(bianry date)'를 의미한다.
