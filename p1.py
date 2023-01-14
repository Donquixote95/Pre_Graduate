# 1. 숫자의 종류 세기
numbers = list((input("integers>")))
counter = {}
# print(numbers)
# for i in range(len(numbers)):
#     print("i".isdigit()) # 결과 : False
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# print(numbers)
for number in numbers:
    if number not in counter:
        counter[number] = 1
    else:
        counter[number] = counter[number] + 1
print(counter)