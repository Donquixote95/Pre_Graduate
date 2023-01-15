# 재귀 함수
# factorial
 # 1. 반복문으로 팩토리얼 구하기
 # 2. 재귀 함수로 팩토리얼 구하기

# 반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))
print()

# 초깃값은 연산자의 항등원(Identity Elemnet)으로 한다.

# 재귀 함수로 팩토리얼 구하기
# recursion(재귀) ; 자기 자신을 호출하는 것

# factorial(n) = n * factorial(n-1) 단, n >= 1
# factorial(0) = 1
def factorial(n):
    # n이 0이라면 1을 리턴
    if n == 0:
        return 1
    # n이 자연수라면 n*(n-1)!을 리턴
    else:
        return n * factorial(n-1)
# 함수 호출
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

# 재귀함수의 문제 ; 상황에 따라서 같은 것을 기하급수적으로 반복한다.
# memoization(메모화) 라는 기술을 통해 해결한다.
# fibonacci_recursion (피보나치 수열을 재귀함수로 구현)
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))

# fibonacci_recursion(2)
# 변수 선언
counter = 0
# 함수 선언
def fibonacci(n):
    # 어떤 피보나치 수를 구하는지 출력
    print("fiboacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    # 피보나치 수를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print("---")
print(f"fibonacci(10) 계산에 활용된 덧셈 횟수는 {counter}입니다.")
# 계산이 기하급수적으로 늘어나는 이유는 Tree 형태의 그림을 보고, node와 leaf를 확인해보면 된다.

# UnboundLocalError, 예외 출력 / 위 함수에서 global을 지우면 나오는 에러
# reference(참조) ; 변수에 접근하는 것
# 파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못한다.
"""
함수 내부에서 함수 외부에 있는 변수라는 것을 설명하려면 다음과 같은 구문을 사용한다.

 global 변수 이름

glboal 키워드는 파이썬 프로그래밍 언어에만 있는 특이한 구조이다. 
"""

# 메모화 ; 피보나치 수열의 재귀함수에서 같은 값을 구하는 연산을 반복하기 때문에 느려진다. 따라서 같은 값을 한 번만 계산하도록 하면 문제를 해결할 수 있다.
# 메모 변수를 만든다.
dictionary = {
    1: 1,
    2: 1
}

# 함수를 선언한다.
def fibonacci(n):
    if n in dictionary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output
# 함수 호출
print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))

# memo(메모) ; 딕셔너리를 사용해서 한 번 계산한 값을 저장, 주로 재귀함수와 함께 사용하는 기술

# early returns(조기 리턴) ; 중간에 return 키워드를 사용, 들여쓰기 단계가 줄기 떄문에 코드를 더 쉽게 읽을 수 있다.

def fibonacci(n):
    if n in dictionary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    # 메모되어 있지 않으면 값을 구함
    output = fibonacci(n-1) + fibonacci(n-2)
    dictionary[n] = output
    return output