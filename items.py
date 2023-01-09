# 딕셔너리의 items() 함수와 반복문 조합하기
# enumerate() 함수와 반복문을 조합해서 for i, value in enumerate(리스트) 형태로 반복문을 작성할 수 있었던 것처럼
# 딕셔너리는 items() 함수와 함께 사용하면 키와 값을 조합해서 쉽게 반복문을 작성할 수 있다.

#딕셔너리의 items() 함수와 반복문
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

print(example_dictionary)

# 딕셔너리의 items() 함수 결과 출력하기
print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

# for 반복문과 items() 함수 조합해서 사용하기
print("# 딕셔너리의 itmes() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))