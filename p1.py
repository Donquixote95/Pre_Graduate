# 1. 숫자의 종류 세기
numbers = list((input("integers>")))
counter = {}
# ex ; 123412314123

# print(numbers)
# for i in range(len(numbers)):
#     print("i".isdigit()) # 결과 : False
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# print(numbers)

# 내가 작성
""" 
for number in numbers:
    if number not in counter:
        counter[number] = 1
     else:
        counter[number] = counter[number] + 1
"""

# 답지 버전
for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1
    
print("사용된 숫자의 종류는", len(counter),"개 입니다.")
print("참고", counter)