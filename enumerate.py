#git log --oneline --all --graph

# enumerat() 함수 ; 리스트의 요소를 반복할 때 현재 인덱스가 몇 번째인지 확인해야 하는 경우 사용

#변수 선언
example_list = ["elementA", "elementB", "elementC"]

#출력
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수를 적용해서 출력
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환해 출력
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerate() 함수 조합해서 사용하기
print("# 반복문과 조합하기")
for i, value in enumerate(example_list): # enumerate() 함수를 사용하면 for 와 in 사이에 반복 변수를 두 개 넣을 수 있다.
    print("{}번쨰 요소는 {}입니다.".format(i, value))