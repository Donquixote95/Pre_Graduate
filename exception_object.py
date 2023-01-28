# exception object ; 예외 객체
"""
try:
    예외가 발생할 가능성이 있는 구문
except 예외의 종류 as 예외 객체를 활용할 변수 이름:
    예외가 발생했을 때 실행할 구문
"""

# Excpetion class

# %%
try:
    number_input_a=int(input("integer> "))
    print("radius:", number_input_a)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

#%%
list_number = [52,273,32,72,100]
try:
    number_input = int(input("integer> "))
    print(f"{list_number}번째 요소: {list_number[number_input]}")
except Exception as exception:
    #예외 객체 출력
    print("type(exception):", type(exception))
    print("exception:", exception)
#%%
# 예외 구분하기
try:
    예외가 발생할 가능성이 있는 구분
except 예외의 종류A:
    예외A가 발생했을 때 실행할 구문
except 예외의 종류B:
    예외B가 발생했을 때 실행할 구문
except 예외의 종류C:
    예외C가 발생했을 때 실행할 구문
# %%
list_number = [52,273,32,72,100]
try:
    number_input = int(input("integer> "))
    print(f"{list_number}번째 요소: {list_number[number_input]}")
except ValueError:
    #ValueError가 발생하는 경우
    print("정수를 입력해주세요.")
except IndexError:
    print("Out of index range.")
# %%
# 예외를 구분할 때 각각의 except 구문 뒤에 예외 객체를 붙여 활용하기. as 키워드
list_number = [52,273,32,72,100]
try:
    number_input = int(input("integer> "))
    print(f"{number_input}번째 요소: {list_number[number_input]}")
except ValueError as exception1:
    #ValueError가 발생하는 경우
    print("정수를 입력해주세요.")
    print("exception:", exception1)
except IndexError as excpetion2:
    print("Out of index range.")
    print("exception:", excpetion2)
# %%
# 예외 처리를 했지만 예외를 못 잡는 경우
list_number = [52,273,32,72,100]
try:
    number_input = int(input("integer> "))
    print(f"{number_input}번째 요소: {list_number[number_input]}")
    예외.발생해주세요()
except ValueError as exception1:
    #ValueError가 발생하는 경우
    print("정수를 입력해주세요.")
    print("exception:", exception1)
except IndexError as excpetion2:
    #IndexError가 발생하는 경우
    print("Out of index range.")
    print("exception:", excpetion2)
# %%
# 위와 같이 예외가 발생하면 프로그램이 강제 종료된다. 그렇기 때문에 else 구문처럼
# 마지막에는 모든 예외를 잡을 수 있는 Exception을 넣어서 프로그램의 강제 종료를 막는다.
list_number = [52,273,32,72,100]
try:
    number_input = int(input("integer> "))
    print(f"{number_input}번째 요소: {list_number[number_input]}")
    예외.발생해주세요()
except ValueError as exception1:
    #ValueError가 발생하는 경우
    print("정수를 입력해주세요.")
    print("exception:", exception1)
except IndexError as excpetion2:
    #IndexError가 발생하는 경우
    print("Out of index range.")
    print("exception:", excpetion2)
except Exception as exception_else:
    #이외의 예외가 발생하는 경우
    print("예상하지 못 한 에러가 발생했습니다.")
    print(type(exception_else), exception_else)
# %%
# raise 구문 ; 예외를 강제로 발생시키는 기능
# raise 예외 객체
# 아직 구현되지 않은 부분에서 강제로 예외 발생시키기

number = input("input> ")
number = int(number)
# 조건문 사용
if number > 0:
    # 양수일 때: 아직 미구현 상태
    raise NotImplemented
else:
    # 음수일 때: 아직 미구현 상태
    raise NotImplemented