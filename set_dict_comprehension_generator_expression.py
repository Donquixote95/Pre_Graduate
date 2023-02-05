# set
a = {1,2,3}
b = {2,3,4}
# ordering is irrelevant
c = {1,1,1,1,2,2,2,}
print(c)

# set의 연산자
# |(합집합)
print("a|b", a|b)
# &(교집합)
print("a&b", a&b)
# -(차집합)
print("a-b", a-b)
print("b-a", b-a)
# ^(대칭차집합)
print("a^b", a^b)
print("a|b - a&b", (a|b) - (a&b)) 

# 세트를 이용해서 중복을 제거하는 예시 ; for 반복문, add() 함수
# 세트를 만들 때 중괄호를 사용하면 딕셔너리가 만들어진다. set() 함수 활용

goal_set = set() #empty set
schools = [
    'A school', 'B school', 'C school',\
    'A school', 'C school', 'C school',\
    'D school'
    ]

for school in schools:
    goal_set.add(school)

print(f"{len(goal_set)}개 학교, {goal_set}")

# for 반복문, add() 함수 대신 update() 함수 사용 ; 리스트를 한꺼번에 읽어 들인다.
goal_set = set() #empty set
schools = [
    'A school', 'B school', 'C school',\
    'A school', 'C school', 'C school',\
    'D school'
    ]
goal_set.update(schools)
print(f"{len(goal_set)}개 학교, {goal_set}")

# 또는 리스트를 set() 함수에 바로 넣어도 된다. 리스트가 세트 자료형으로 변환된다.
schools = [
    'A school', 'B school', 'C school',\
    'A school', 'C school', 'C school',\
    'D school'
    ]
goal_set = set(schools)
print(f"{len(goal_set)}개 학교, {goal_set}")


# 리스트 내포의 기본 구조
[
    item * item  #(1) 요소로 만들 부분
    for item in range(0,10) #(2) 반복문 부분
    if item % 2 == 0 #(3) 조건문 부분
]

#(1) 요소로 만들 부분: 이 부분에 작성한 값이 최종 리스트에 들어간다. 반복 변수를 활용해서 값을 만들 수 있다. 기본적으로 map() 함수 역할
#(2) 반복문 부분 : 반복문 부분에서는 반복 가능한 것을 기반으로 반복하며 반복 변수를 설정, 위 코드에서는 range(0, 10)을 item이라는 반복 변수로 반복
#(3) 조건문 부분 : 반복 변수를 조건으로 필터링한다. 기본적으로 filter() 함수 역할이다.

# 딕셔너리 내포(dictionary comprehension)
a = {
    f"키_{item}" : item*item
    for item in range(0, 10)
    if item % 2 == 0
}
print(type(a))
print(a)
print()

# 세트 내포(set comprehension)
b = {
    item*item
    for item in range(0, 10)
    if item % 2 == 0
}
print(type(b))
print(b)
print()

# generator expression(제너레이터 표현식)
# 리스트 내포의 괄호를 소괄호로 변경

c = (
    item * item  
    for item in range(0,10) 
    if item % 2 == 0 
    )
print(type(c))
print(c) # generator가 출력된다.
print()

# 함수의 괄호로 둘러싸인 경우에는 () 괄호를 사용하지 않아도 제너레이터 표현식으로 인식한다.
print(
    item * item  
    for item in range(0,10) 
    if item % 2 == 0 
)

"""
제너레이터 표현식은 대부분의 상황에서 리스트 내포를 대체할 수 있다.
가능하면 대체하는 것이 더 좋다.
리스트 내포는 새로운 리스트를 하나 더 만들어낸다.(copy)
그래서 메모리에 큰 부담을 준다.

제너레이터 표현식은 제너레이터를 만든다. 리스트를 하나 더 만들지 않는다.
원본 리스트를 보고 처리하므로 메모리에 큰 부담을 주지 않는다.
그러나 리스트 내포를 제너레이터 표현식으로 대체하면 안 되는 경우가 있다.
"""

# 예외 1. 미리 처리해 두고 요청이 있을 때 곧바로 데이터를 응답해야 하는 상황
# 리스트 내포와 제너레이터 표현식은 처리되는 시점이 다르다.
# 리스트 내포는 리스트 내포 코드를 사용하는 시점에 처리된다.
original = [1,2,3,4,5,6]
list_comprehension = [str(i) for i in original] # 처리된다.
print(",".join(list_comprehension))
print()

original = [1,2,3,4,5,6]
genorator_expression = (str(i) for i in original)
print(",".join(genorator_expression)) # 처리된다. 