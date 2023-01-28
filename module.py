# module(모듈) ; 여러 변수와 함수를 가지고 있는 집합체

# (1) 표준 모듈 ; 파이썬에 기본적으로 내장되어 있는 모듈

# (2) 외부 모듈 ; 다른 사람들이 만들어서 공개한 모듈

# import 구문 ; 모듈을 가져온다. 코드의 가장 위에 작성한다.
""" 
import 모듈 이름
"""

import math

math.sin(1)
math.cos(1)
math.tan(1)
math.floor(2.5) # 내림
math.ceil(2.5) # 올림
math.log(3,[math.e])

# 실수를 정수로 변환하는 가장 쉬운 방법은 math 모듈의 floor() 함수와, ceil() 함수 사용
# round() 함수 ; 반올림을 유사하게 하는 함수. 정수 부분이 짝수일 때 소수점이 5라면 내리고, 홀수일 때 소수점이 5라면 올리는 방식

round(1.5)
round(2.5)
round(3.5)
round(4.5)

# from 구문
"""
from 모듈 이름 import 가져오고 싶은 변수 또는 함수
"""
from math import sin, cos, tan, floor, ceil
sin(1)
cos(1)
tan(1)
floor(1.5)
ceil(1.5)

# 모두 가져오기
from math import *

# as 구문 ; 모듈의 이름을 줄여서 짧게 사용하고 싶을 경우, 모듈을 가져올 때 식별자 이름에서 충돌을 방지하는 경우
"""
import 모듈 as 사용하고 싶은 식별자
"""

import math as m
m.sin(1)
m.cos(1)
m.tan(1)
m.floor(1.5)
m.ceil(2.5)