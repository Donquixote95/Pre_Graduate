# 튜플, 람다, 파일처리는 파이썬의 특별한 문법이다.
# tuple(튜플) ; 함수와 함께 많이 사용되는 리스트와 비슷한 자료형, 리스트와 다른 점은 한번 결정된 요소는 바꿀 수 없다.
# lambda(람다) ; 매개변수로 함수를 전달하기 위해 함수 구문을 작성하는 것이 번거롭고, 코드 공간 낭비라는 생각이 들 때 함수를 간단하고 쉽게 선언하는 방법
#               1회용 함수를 만들어야 할 떄 많이 사용.

"""
튜플은 다음과 같은 형태로 생성한다.
(데이터, 데이터, 데이터, ...)
"""
tuple_test = (10, 20, 30)
print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])

# 요소를 변경할 때 리스트와 차이가 있다. 다음과 같은 식은 오류가 생긴다. 튜플은 내부 요소 변경이 불가능하다.
# tuple_test[0] = 1

"""
요소를 하나만 가진 리스트는 다음과 같은 형태로 생성
[273]

요소를 하나만 가지는 튜플은 어떻게 생성할까? 다음과 같이 생성해서는 안 된다.(X)
(273)
273이라는 숫자를 괄호로 감싼 것으로 인식하기 떄문이다.

요소를 하나만 가지는 튜플을 선언하려면 다음과 같이 쉼표를 넣어 선언한다.(O)
(273,)
"""

# 괄호 없는 튜플
# 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)

# 출력합니다.
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# 리스트와 튜플은 위와 같은 형태로 변수를 선언하고 할당할 수 있따.
# 그런데 튜플은 다른 성질도 있다. 괄호를 생략해도 튜플로 인식할 수 있는 경우는 괄호를 생략해도 된다.

# 괄호 없는 튜플
tuple_test = 10, 20, 30, 40
print("# 괄호 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

# 괄호가 없는 튜플 활용
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)
print()

# 변수의 값을 교환하는 튜플
a, b = 10, 20

print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()

# 값을 교환한다.
a, b = b, a

print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()

# 튜플과 함수
"""
튜플은 함수의 리턴에 많이 사용한다.
함수의 리턴에 튜플을 사용하면 여러 개의 값을 리턴학도 할당할 수 있기 때문이다.
"""
# 여러 개의 값 리턴하기
# 함수 선언
def test():
    return (10, 20)

# 여러 개의 값을 리턴 받는다.
a, b = test()

# 출력한다.
print("a:", a)
print("b:", b)
print()

# 튜플도 리스트처럼 +와 *연산자 등을 활용할 수 있다. 그러나 리스트와 작성하는 것과 차이가 없어서 튜플로 만드는 경우가 적다.
# 괄호 없이 여러 값을 할당하는 것은 튜플로만 할 수 있는 일이다.

# 튜플을 리턴하는 함수의 예
"""
for i, value in enumerate([1,2,3,45,5,6]):
    위에서 i, value가 괄호 없는 튜플이다.
"""

# 목과 나머지를 구하는 divmod() 함수도 튜플을 리턴하는 대표적인 함수다.
a, b = 97, 40
print(a // b) # 몫
print(a % b) # 나머지
print()

# 몫과 나머지이므로 두 가지 값이 나온다. divmod() 함수는 이에 따라 튜플 형태로 몫과 나머지를 리턴한다.
a, b = 97, 40
print(divmod(a, b))
x, y = divmod(a, b)
print(a)
print(b)


# 람다(lambda) ; 함수라는 '기능'을 매개변수로 전달하는 코드를 많이 사용하는데 이런 코드를 조금 더 효율적으로 작성하기 위한 것
# callback function(콜백 함수) ; 함수의 매개변수에 사용하는 함수

# 함수를 매개변수로 함수 전달하기
# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수
def print_hello():
    print("Hello")

# 조합하기
call_10_times(print_hello) # 매개변수로 함수를 전달


# 표준 함수(내장 함수) ; 파이썬이 표준으로 제공하는 함수

# 함수를 매개변수로 사용하는 대표적인 표준 함수는 map() 함수와 filter() 함수

# map() 함수는 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수
# map(함수, 리스트)

# filter() 함수는 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트를 구성해주는 함수
# filter(함수, 리스트)

# map() 함수와 filter() 함수
# 함수를 선언
def power(item):
    return item * item
def under_3(item):
    return item < 3

# 변수를 선언
list_input_a = [1,2,3,4,5]

# map() 함수를 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter() 함수를 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print()

# 결과로 <map object>와 <filter object>가 나온다. 이를 generator(제너레이터)라고 부른다.

# 람다의 개념 ; 간단한 함수를 쉽게 선언하는 방법, 매개변수로 함수를 전달하기 위해 함수 구문을 작성하는 것도 번거롭고 코드 공간 낭비라서 생겼다.
"""
lamda 매개변수: 리턴값
"""
# 람다로 변환, def 키워드로 선언했던 함수를 lambda로 바꾸고, return 키워드를 따로 쓰지 않는다.
# 함수를 선언
power = lambda x: x * x
under_3 = lambda x: x < 3

# 변수를 선언
list_input_a = [1,2,3,4,5]

# map() 함수를 사용
output_a = map(power, list_input_a)
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter() 함수를 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print()

# 인다인 람다 ; 함수의 매개변수에 곧바로 넣는 방법
# 변수를 선언
list_input_a = [1,2,3,4,5]

# map() 함수를 사용
output_a = map(lambda x: x*x, list_input_a)
print("map(lambda x: x*x, list_input_a):", output_a)
print("map(lambda x: x*x, list_input_a):", list(output_a))
print()

# filter() 함수를 사용
output_b = filter(lambda x: x<3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(lambda x: x<3, list_input_a):", output_b)
print("filter(lambda x: x<3, list_input_a):", list(output_b))
print()
