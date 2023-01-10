# 반복문을 사용한 리스트 생성

# 변수 선언
array = []

# 반복문을 적용
for i in range(0, 20, 2):
    array.append(i * i)
print(array)

#리스트 안에 for문 사용하기
array=[i*i for i in range(0,20,2)] #최종 결과를 앞에 작성한다.

#출력한다
print(array)

"""
range(0, 20, 2)의 요소를 i라고 할 때, i*i로 리스트를 재조합해주세요 라는 코드이다.

이런 구문을 리스트 내포 list comprehensions 라고 부른다.

리스트 내포의 형태
리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]

다음과 같이 뒤에 if 구문을 넣어 조건을 조합할 수도 있다.
리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
"""

# array comprehensions
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)
#array의 요소를 초콜릿이 아닌 fruit로 리스트를 재조합한다. 라는 코드이다.

"""
한 줄로 입력했을 때 코드가 너무 길어서 코드 가독성이 떨어지면 3줄로 작설할 수도 있다.
리스트 이름 = [표현식
    for 반복자 in 반복할 수 있는 것
    if 조건문]

ex)
output = [fruit
    for fruit in array
    if fruit != "초콜릿"]
"""

# 구문 내부에 여러 줄의 문자열을 만들면 들여쓰기(indent)가 들어간다.
number = int(input("integer>"))
# if 조건문으로 홀수 짝수를 구분
if number % 2 == 0:
    print("""
    입력한 문자열은 {}입니다.
    {}는(은) 짝수입니다.
    """.format(number, number))
else:
    print("""\
    입력한 문자열은 {}입니다.
    {}는(은) 홀수입니다.
    """.format(number, number))

# 한 줄로 고쳐 쓰거나, 들여쓰기를 안 하면 정상적으로 출력이 된다.
# 다른 방법 1. 괄호로 문자열 연결하기

# 변수 선언
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성된다."
)
print("test:", test)
print("type(test):",type(test))
# 위 자료형은 tuple 이 아니다. tuple(튜플) 이려면 괄호 내부의 문자열이 쉼표로 연결되어야 한다.
# 줄바꿈을 하려면 마지막을 제외한 문자열 뒤에 \n을 입력하면 된다.

# 변수 선언
number = int(input("integer>"))
# if 조건문으로 홀수 짝수를 구분
if number % 2 == 0:
    print((
    "입력한 문자열은 {}입니다.\n"
    "{}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
    "입력한 문자열은 {}입니다.\n"
    "{}는(은) 홀수입니다."
    ).format(number, number))

# 다른 방법 2. 문자열의 join() 함수
# 문자열.join(문자열로 구성된 리스트)

print("::".join(["1", "2", "3", "4", "5"]))

number = int(input("integer>"))
# if 조건문으로 홀수 짝수를 구분
if number % 2 == 0:
    print("\n".join([
    "입력한 문자열은 {}입니다.",
    "{}는(은) 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
    "입력한 문자열은 {}입니다.",
    "{}는(은) 홀수입니다."
    ]).format(number, number))

# way 1. git push -f origin master

# way 2. git pull origin master