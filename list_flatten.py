# 리스트가 중첩되었을 때 중첩을 제거하는 처리를 list_flatten(리스트 평탄화)라고 한다.


# 내 풀이 - 파괴적 방법
"""
a_list = [1, 2, [3, 4], 5, [6, 7], [8, 9]]

for item in a_list:
    if type(item) == list:
        a_list.extend(item)
        a_list.remove(item)
for item in a_list:
    if type(item) == list:
        a_list.extend(item)
        a_list.remove(item)
a_list.sort()
print(a_list)
"""

# 답지 풀이 - 비파괴적 방법
a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
output = []

for i in a:
    if type(i) == list:
        # 요소가 리스트라면 요소를 추가
        for j in i:
            output.append(j)
    else:
        # element가 number라면 추가
        output.append(i)

print(f"{a}를 평탄화하면")
print(f"{output}입니다.")