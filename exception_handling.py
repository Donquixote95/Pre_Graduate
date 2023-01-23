"""
Error의 종류

1. Syntax Error(구문 오류) ;  프로그램 실행 전에 발생하는 오류

2. Runtime Error(런타임 오류) ; exception(예외) ;  프로그램 실행 중에 발생하는 오류

"""

"""
syntax error는 해결하지 않으면 프로그램 자체가 실행되지 않는다.
따라서 예외 처리 방법으로 처리할 수 없다.
문법 문제가 발생한 코드를 수정해야 한다.

excpetion handling(예외 처리) ; 예외를 해결하는 모든 것
 1. 조건문을 사용하는 방법 ; 기본 예외 처리
 2. try 구문을 사용하는 방법
"""

# handle_with_condition
from math import pi
"""
# input number
user_input_a = input("integer> ")

# if condition
if user_input_a.isdigit():
    # transform to num
    user_input_a = int(user_input_a)
    # print
    print("radius: ", user_input_a)
    print("round: ", pi * user_input_a)
    print("arae: ", pi * (user_input_a)**2)
else:
    print("You are not input the integer")
"""

# try except ; 어떤 상황에 예외가 발생하는지 완벽하게 이해하고 있지 않아도 프로그램이 실행되지 않는 상황을 막을 수 있다.
"""
try:
    예외가 발생할 가능성이 있는 코드
except:
    예외가 발생했을 때 실행할 코드
"""
# e.g. try excpet
try:
    # input number and transform int
    user_input_a = int(input("integer> ")) # 예외가 발생할 가능성이 있는 구문
    # 출력
    print("radius: ", user_input_a)
    print("round: ", pi * user_input_a)
    print("arae: ", pi * (user_input_a)**2)
except:
    print("Something is wrong.")

# try excpet 구문과 pass 키워드 조합 ; 이유는 정확하게 모르지만, 어떤 부분에서 예외가 발생하는지 정도는 파악할 수 있을 때 사용
                                    # 일단 예외를 처리해야 하지만, 해당 코드가 딲히 중요한 부분이 아니라면 프로그램이 강제 종료되는 것부터 막는 목적
                                    # 구문 내부에 아무 것도 넣지 않으면 구문 오류가 발생하므로 다음과 같이 pass 키워드를 넣는다.
"""
    try:
    예외가 발생할 가능성이 있는 코드
excpet:
    pass
"""
# 변수 선언
list_input_a = ["52", "273", "32", "spy", "103"]

# 반복 적용
list_number = []
for item in list_input_a:
    # 숫자로 변환해서 리스트에 추가
    try:
        float(item) # 예외가 발생하면 알아서 다음으로 진행이 안 된다.
        list_number.append(item) # 예외 없이 통과했으면 list_number 리스트에 넣기
    except:
        pass
# 출력
print(f"{list_input_a} 내부에 있는 숫자는")
print(f"{list_number} 입니다.")


# try excpet else 구문 ; else 구문을 붙여서 사용하면 '예외가 발생하지 않았을 때 실행할 코드'를 지정할 수 있다.
                        # 예외가 발생할 가능성이 있는 코드만 try 구문 내부에 넣고 나머지 모두 else 구문으로 뺴는 경우가 많다.
"""
try:
    예외가 발생할 가능성이 있는 코드
excpet:
    예외가 발생했을 때 실행할 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
"""

# try except else 구문으로 예외를 처리
try:
    user_input_a = int(input("integer> ")) # 예외가 발생할 가능성이 있는 구문
except:
    print("Something is wrong.")
else:
    # 출력
    print("radius: ", user_input_a)
    print("round: ", pi * user_input_a)
    print("arae: ", pi * (user_input_a)**2)


# finally 구문 ; 예외 처리 구문에서 가장 마지막에 사용할 수 있는 구문
                # 예외가 발생하든 발생하지 않든 무조건 실행할 때 사용하는 코드

"""
try:
    예외가 발생할 가능성이 있는 코드
excpet:
    예외가 발생했을 때 실행할 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    무조건 실행할 코드
"""
# try except 구문으로 예외를 처리
try:
    # 숫자로 변환
    user_input_a = int(input("integer> "))
    # 출력
    print("radius: ", user_input_a)
    print("round: ", pi * user_input_a)
    print("arae: ", pi * (user_input_a)**2)
except:
    print("Something is wrong.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("program is done, somehow.")