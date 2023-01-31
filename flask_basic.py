# %%
from flask import Flask
app = Flask(__name__)

@app.route("/") #decorator(함수 데코레이터)
def hello():
    return "<h1>Hello world!</h1>"

# 다음 두 줄을 터미널에서 입력한다.
# $env:FLASK_APP="파일 이름"
# flask run

# 맥 또는 리눅스에서는 터미널에 아래와 같이 입력한다.
# export FLASK_APP=파일 이름.py
# flask run

# 명령 프롬프트에서는 "set FLASK_APP=파일 이름"을 이용한다.

# %%
# 모듈 읽기
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 경기도 날씨 읽기
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

    # BeautifulSoup를 사용해서 웹페이지 분석
    soup = BeautifulSoup(target, "html.parser")

    # location 태그 찾기
    output = ""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력하기
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저, 최고 기온: {}, {}"\
            .format(\
            location.select_one("tmn").string,\
            location.select_one("tmx").string\
            )
        output += "<hr/>"
    return output