from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 경기 날씨를 읽는다.
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

# BeautifulSoup를 사용해 웹페이지를 분석한다
soup = BeautifulSoup(target, "html.parser")

# location 태그를 찾는다.
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력한다.
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()

# 태그를 여러 개 선택할 때는 select() 함수
# 태그를 하나만 선택할 떄는 select_one() 함수를 사용해서 원하는 값을 추출한다.