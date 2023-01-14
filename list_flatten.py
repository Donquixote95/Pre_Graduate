# 리스트가 중첩되었을 때 중첩을 제거하는 처리를 list_flatten(리스트 평탄화)라고 한다.

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