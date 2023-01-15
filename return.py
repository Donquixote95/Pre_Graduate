# return value(리턴값)

# return 키워드 ; 함수 내부에서 사용. 함수를 실행했던 위치로 돌아가라는 뜻, 함수가 끝나는 위치를 의미

# 자료 없이 리턴하기
def return_test():
    print("A 위치입니다.")
    return
    print("B위치입니다.")
return_test()

# 자료와 함께 리턴하기
# 리턴 뒤에 자료를 입력하면 자료를 가지고 리턴한다.
def return_test():
    return 100
value = return_test()
print(value)

# 아무것도 리턴하지 않기
def return_test():
    return
value = return_test()
print(value) # None


# 기본적인 함수의 활용
"""
def 함수(매개변수):
    변수 = 초깃값
    # 여러 가지 처리
    # 여러 가지 처리
    retrun 변수
"""

# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    # 변수 선언
    output = 0
    # 반복문을 돌려 숫자를 더하기
    for i in range(start, end+1):
        output += i
    # 리턴
    return output
# 함수 호출
print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))

# 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start=0, end=100, step=1):
    # 변수 선언
    output=0
    # 반복문
    for i in range(start, end+1, step):
        output += i
    return output
print("A.", sum_all(0,100,10))
print("B.", sum_all(end=100))
print("c.", sum_all(end=100, step=2))

# 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수
def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output
print(mul(5,7,9,10))