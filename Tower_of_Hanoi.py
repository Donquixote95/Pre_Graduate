numbers = [1,2,3,4,5,6]

print("::".join(map(str,numbers)))

# 위 코드에서 map 함수와 str 함수 없이 numbers를 넣으면
# TypeError: sequence item 0: expected str instance, int found 라는 오류가 발생한다.
# 문자열이 들어있을 것으로 예상했는데, 숫자가 들어있다는 의미
# 즉, 리스트 내부의 모든 숫자를 문자열로 변환해야 한다.

numbers = list(range(1, 10 + 1))

print("# Odd number filter")
print(list(filter(lambda x: x%2==1,numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3<=x<7,numbers)))
print()

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda x: x**2 < 50 , numbers)))
print()