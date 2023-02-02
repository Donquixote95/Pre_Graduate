# library : 정상적인 제어를 하는 모듈

# framework : 제어 역전이 발생하는 모듈

# IoC(Inversion of Control, 제어역전) : 제어가 역전되는 것, 개발자가 만든 함수를 모듈이 실행하는 것

# 라이브러리 ; 개발자가 모듈의 기능을 호출하는 형태의 모듈
# 일반적인 제어 흐름은 개발자가 모듈의 함수를 호출한다.
# e.g. math 모듈

# 프레임 워크 ; 모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈
# e.g. flask 모듈 ; 내부에 함수만 정의했지 직접적으로 무언가 진행하는 코드는 없음 

# Decorator(데코레이터)
# - 함수 데코레이터
# - 클래스 데코레이터

# 함수 데코레이터 ; 대상 함수의 앞뒤에 꾸밀 부가적인 내용, 혹은 반복할 내용을 데코레이터로 정의해서 손쉽게 사용할 수 있도록 한 것
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.") 
    return wrapper

# 데코레이터를 붙여서 함수를 만든다.
@test
def hello():
    print("hello")

# 함수 호출
hello()

# 데코레이터를 사용하면 functools라는 모듈을 사용할 수 있고, 
# 매개변수 등을 전달할 수 있어 반복되는 구문이 많아질 때 소스의 가독성을 높일 수 있다.

from functools import wraps

# 함수 데코레이터를 생성한다.
def test(function):
    @wraps(function)
    def wrapper(*arg, **kwargs): #가변 매개변수와 키워드 가변 매개변수
        print("인사 시작")
        function(*arg, **kwargs)
        print("인사 종료")
    return wrapper

# 패키지 ; 모듈을 구조화해서 거대해진 것