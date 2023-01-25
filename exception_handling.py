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

# 예외 처리 구문(try, except, finally)의 조합 규칙
"""
1. try 구문은 단독으로 사용할 수 없다. 반드시 except 구문 또는 finally 구문과 함께 사용해야 한다.
2. else 구문은 반드시 except 구문 뒤에 사용해야 한다.
3. 위 규칙을 지키지 않으면 'SyntaxError: Invalid syntax'
e.g.
 - try + except
 - try + except + else
 - try + except + finally
 - try + except + else + finally
 - try + finally

"""

# 파일이 제대로 닫혔는지 확인하기, file 객체의 closed 속성으로
try:
    # open file
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    # 파일을 닫기
    file.close()
except:
    print("error occurr")

print("# 파일이 제대로 닫혔는지 확인")
print("file.closed: ", file.closed) #True

# daemon(데몬), Service(서비스); 항상 켜져 있는 프로그램

# 파일을 닫을 때 close() 함수를 사용하지만, 중간 과정에서 예외가 발생해서 try 구문 중간에 튕겨 버리면 파일이 제대로 닫히지 않는 문제가 발생할 수 있다.
try:
    # open file
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    error.occur()
    # 파일을 닫는다.
    file.close()
except:
    print("error occurr")

print("# 파일이 제대로 닫혔는지 확인")
print("file.closed: ", file.closed) #False

#따라서 finally 구문을 사용해서 오류가 발생하더라도 닫게 하면 좋다.
try:
    # open file
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    error.occur()
except:
    print("error occurr")
finally:
    # 파일을 닫는다.
    file.close()
print("# 파일이 제대로 닫혔는지 확인")
print("file.closed: ", file.closed) #True

#try, except 구문이 끝난 후 파일 닫기 ; 가능하며 문제 없음. finally 키워드를 무조건 사용할 필요가 없음.
try:
    # open file
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    error.occur()
except:
    print("error occurr")

# 파일을 닫는다.
file.close()
print("# 파일이 제대로 닫혔는지 확인")
print("file.closed: ", file.closed)

#try 구문 내부에서 return 키워드를 사용하는 경우
#test() 함수를 선언
def test():
    print("test() 함수의 첫 줄")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문 실행")
    else:
        print("else 구문 실행")
    finally:
        print("finally 구문 실행")
    print("test() 함수의 마지막 줄")

#test함수 호출
test() # 실험해보면 finally 구문은 try 구문 내부에서 return해도 실행된다.

#finally 키워드 활용
def write_text_file(filename, text):
    try:
        #파일 열기
        file = open(filename, "w")
        #여러 가지 처리 수행
        return
        #파일에 텍스트 입력
        file.write(text)
    except:
        print("error")
    finally:
        # 파일 닫기
        file.close()
#함수 호출
write_text_file("test.txt", "안녕!")


# finally 구문은 무조건 실행되기 떄문에 반복문에서 break와 함께 사용할 수도 있다.
# %%
print("프로그램 시작")

while True:
    try:
        print("try 구문 실행")
        break
        print("try 구문의 break 키워드 뒤")
    except:
        print("except 구문 실행")
    finally:
        print("finally 구문이 실행")
    print("while 반복문의 마지막 줄")
print("프로그램 종료")

# type hinting 기능을 이용할 때 'value : Any'를 입력하면 "name 'Any' is not defined"라는 오류가 발생한다.
# 해결 1. 
from typing import List, Any
# 해결 2.
# linear_search(L: list, value: any) -> None: 과 같이, lower character로 적는 방법