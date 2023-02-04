# 파일 ; text data, binary data

# 컴퓨터는 내부적으로 모든 처리를 0과 1로 이루어진 binary로 수행한다.

# encoding 방식; 숫자와 알파벳을 대응하는 것
# decoding ; 인코딩된 데이터를 반대로 돌리는 것
# ASCII 인코딩 방식 

# '100' 이라는 글자는 '1', '0', '0,' 이라는 글자로 이루어져 있으며 ASCII 코드표에서 각각 '49', '48', '48'로 변환할 수 있다.

# 따라서 100.txt라는 파일로 저장하면 내부적으로 다음과 같이 저장된다.
# 3바이트를 차지하는 텍스트 데이터 100[49, 48, 48]
# 00110001, 00110000, 00110000

# 100을 '1', '0', '0'으로 나타내는 텍스트 데이터가 아니라 곧바로 '100'이라는 숫자로 저장하는 경우
# 세 글자를 한 글자로 표현할 수 있게 되므로 용량이 절약된다.
# 1바이트를 차지하는 바이너리 데이터 100[100]
# 01100100
# 100이라는 숫자는 ASCII 코드표에서 'd'에 해당된다.

# 문자열 앞에 'b'가 붙어있으면 바이너리 데이터를 의미한다.
# 바이너리 데이터는 문자열(텍스트)이 아니므로 문자열과 관련된 기능(len() 함수 등)을 이용할 수 없다.
# 파이썬은 바이너리를 무조건 ASCII 코드표 등으로 인코딩해서 출력해주기 떄문에 바이너리 데이터라도 글자로 출력된다.

# 이미지를 읽어 들이고 저장하기
from urllib import request

# urlopen() 함수로 특정 출판사의 메인 페이지를 읽는다.
target = request.urlopen("https://s3.marpple.co/files/u_218933/2020/1/original/14474423ccd1acb63fab43dc936ab01302c64b547577e2e.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb") # 바이너리 형식으로 쓴다.
file.write(output)
file.close()

# write text[텍스트 쓰기] 모드로 -> 오류가 생긴다.
file = open("output.png", "w") # 텍스트 쓰기 모드로 쓴다.
file.write(output)
file.close()

# pip list ; 설치된 모듈을 확인할 수 있다.

# pip show <설치된 모듈> ; 모듈이 설치된 위치를 확인할 수 있다.
# location 이 모듈이 설치된 위치다.