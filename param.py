# 함수를 호출한다. ; 함수를 사용하는 것

# 매개변수 ; 함수를 호출할 때 괄호 내부에 넣는 여러 가지 자료

# 리턴값 ; 함수를 호출해서 최종적으로 나오는 결과

# 함수의 기본 ; 함수란 '코드의 집합'

# 함수의 기본 형태
"""
def 함수 이름():
    문장
"""

def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()
print()

# 함수에 매개변수 만들기
# 매개변수는 함수를 생성할 때 괄호 내부에 식별자를 이용해서 만든다.
"""
def 함수 이름(매개변수, 매개변수, ...):
    문장
"""

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

# 가변 매개변수 함수 ; 매개변수를 원하는 만큼 받을 수 있는 함수
"""
def 함수 이름(매개변수, 매개변수, ..., *가변 매개변수):
    문장
"""
# 가변 매개변수의 제약
 # 제약 1. 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
 # 제약 2. 가변 매개변수는 하나만 사용할 수 있다.

def print_n_times(n, *values):
    # n번 반복한다.
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()

# 함수를 호출
print_n_times(3, "Hello", "Fun", "Python Programming")


# 기본 매개변수 ; 매개변수를 입력하지 않았을 경우 매개변수에 들어가는 기본값
# 기본 매개변수의 제약 ; 기본 매개변수 뒤에는 일반 매개변수가 올 수 없다.

def print_n_times(value, n=2):
    # n번 반복
    for i in range(n):
        print(value)
# 함수를 호출
print_n_times("Hello")
print()

# 가변 매개변수와 기본 매개변수 둘을 같이 쓸 때 주의할 점
# 상황 1. 기본 매개변수가 가변 매개변수보다 앞에 올 때 ; 기본 매개변수의 의미가 사라짐

"""
def print_n_times(n=2, *values):
    # n번 반복
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()
# 함수를 호출
print_n_times("Hello", "Fun", "Python")
"""
# 매개변수가 순서대로 입력되므로 n에는 "Hello"가 들어간다. 그렇기 때문에 오류가 발생한다.
# 따라서 기본 매개변수는 가변 매개변수 앞에 써도 의미가 없다.


# 상황 2. 가변 매개변수가 기본 매개변수보다 앞에 올 때
def print_n_times(*values, n=2):
    # n번 반복
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()
# 함수를 호출
print_n_times("Hello", "Fun", "Python", 3)
# 가변 매개변수가 우선되기 떄문에 "Hello", "Fun", "Python", 3이 2번 출력된다.

# 키워드 매개변수 ; 매개변수 이름을 지정해서 입력하는 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("hello", "fun", "python", n=3)

# 기본 매개변수 중에서 필요한 값만 입력하기
def test(a, b=10, c=100):
    print(a + b + c)
# 1) 기본 형태
test(10, 20, 30)
# 2) 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)
# 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)
# 4) 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)