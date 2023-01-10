"""반복문의 구문
for 반복자 in 반복할 수 있는 것

'반복할 수 있는 것'을 프로그래밍 용어로 iterable(이터러블)이라고 한다.

이터러블은 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체를 의미한다. 
리스트, 딕셔너리, 문자열, 튜플 등은 모두 내부에서 요소를 차례차레 꺼낼 수 있으므로 이터러블이다.

이터러블 중에서 next() 함수를 적용해 하나하나 꺼낼 수 있는 요소를 iterator(이터레이터)라고 한다.
"""

# reversed() 함수와 이터레이터
# 변수 선언
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

# reversed_numbers 출력
print("reversed_nubmers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

"""
<list_reverseiterator object at 주소>로 출력된다.
reversed() 함수의 리턴값이 바로 'reverseiterator'로 이터레이터이다.
이터레이터는 반복문의 매개변수로 전달할 수 있으며, next() 함수로 내부의 요소를 하나하나 꺼낼 수 있다.

for 반복문의 매개변수에 넣으면 반복할 떄마다 next() 함수를 사용해서 요소를 하나하나 꺼내준다.
왜 reversed() 함수는 리스트를 바로 리턴해주지 않고 이터레이터를 리턴해주는가?

이는 메모리의 효율성을 위해서다. 1만 개의 요소가 들어 있는 리스트를 복제한 뒤 뒤집어서 리턴하는 것보다
기존에 있던 리스트를 활용해서 작업하는 것이 훨씬 효율적이라고 판단하기 때문이다.
"""