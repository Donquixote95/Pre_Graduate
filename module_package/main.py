# pip : Python Package Index, 패키지 관리 시스템(Package Management System)
# 모듈이 모여서 구조를 이루면 패키지라고 부른다.
# %%
import test_package.module_a as a
import test_package.module_b as b

# 모듈 내부의 변수를 출력
print(a.variable_a)
print(b.variable_b)

# %%
from test_package import *

# 모듈 내부의 변수를 출력
print(module_a.variable_a)
print(module_b.variable_b)

# python 3.3 이전 버전에서는 __init__.py 파일이 무조건 있어야 패키지로 작동했다.
# 이후 버전에서는 __init__.py 파일이 없어도 폴더 내부에 파이썬 파일이 들어 있기만 하면 패키지로 작동한다.