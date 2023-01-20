# generator(제너레이터) ; 이터레이터(iterator)를 직접 만들 때 사용하는 코드
# yield 키워드 ; 함수 내부에 사용하면 해당 함수는 제너레이터 함수가 되며, 일반 함수와 달리 호출해도 함수 내부의 코드가 실행되지 않는다.

# 함수를 선언한다.
def test():
    print("함수가 호출되었습니다.")
    yield "test"

# 함수를 호출합니다.
print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())
print()
# 출력된 <generator object test at 0x0000015F511813C0>는 제너레이터 객체이다. 

# 즉, 제너레이터 함수는 제너레이터를 리턴한다.

# 제너레이터 객체는 next() 함수를 사용해 함수 내부의 코드를 실행한다.
# 이때 yield 키워드 부분까지만 실행하며, next() 함수의 리턴값으로 yield 키워드 뒤에 입력한 값이 출력된다.


# 제너레이터 객체와 next() 함수
# 함수를 선언
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
# 함수를 호출한다.
output = test()
# next() 함수를 호출한다.
print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c) # StopIteration 이라는 예외가 발생한다. next() 함수를 호출한 이후 yield 키워드를 만나지 못하고 함수가 끝나는 경우다.
# 한 번 더 실행하기
next(output) 

# 제너레이터 객체는 함수의 코드를 조금씩 실행할 떄 사용한다. 메모리의 효율성 때문이다.
# 제너레이터 객체와 이터레이터 객체는 완전히 같지는 않다.
# 제너레이터는 직접 이터레이터를 만드는 코드다.