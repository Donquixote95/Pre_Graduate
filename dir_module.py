# %%
import os

# 현재 폴더의 파일/폴더를 출력
output = os.listdir()
print("os.listdir():", output)
print()

# %%
import os
output = os.listdir(".")
# 현재 폴더의 파일과 폴더를 구분
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)

# %%
# 폴더라면 또 탐색하기 
import os
def read_folder(path):
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            # 폴더라면 계속 읽어 들이기
            read_folder(item)
            # read_folder(path+"/"+item)과 차이점을 모르겠음.
    else:
        # 파일이라면 출력하기
        print("파일:", item)

# 현재 폴더의 파일과 폴더 출력
read_folder(".")