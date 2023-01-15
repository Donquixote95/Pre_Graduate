def flatten(data):
    output = []
    for item in data:
        if type(item) != list:
            output.append(item)
        else:
            output += item
    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("Original:", example)
print("Transform:", flatten(example)) # 완벽하게 평탄화되지 않음

# 재귀 함수 적용
def flatten(data):
    output = []
    for item in data:
        if type(item) != list:
            output.append(item)
        else:
            output += flatten(item) # flatten 함수를 재귀적으로 호출
    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("Original:", example)
print("Transform:", flatten(example))

# 기억해야 할 것
"""
1. 함수의 변수는 함수 호출마다 따로따로 만들어진다.
faltten() 함수에서 flatten() 함수를 호출했을 때 변수 output이 계속해서 이어진다고 생각하면 안 된다.
함수의 변수는 함수 호출마다 따로 만들어지낟.

2. 함수가 끝나면(리턴되면) 함수를 호출했던 위치로 돌아온다.
output += flatten(item) 부분에서 재귀적으로 flatten() 함수를 호출한다.
"""