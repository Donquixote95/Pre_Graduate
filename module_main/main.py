# main.py 파일
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# 모듈의 __name__
# 엔트리 포인트가 아니지만 엔트리 포인트 파일 내에서 import 되었기 때문에
# 모듈 내 코드가 실행된다. 모듈 내부에서 __name__을 출력하면 모듈의 이름을 나타낸다.

# %%
# 모듈 이름을 출력하는 모듈 만들기
import test_module

print("# 메인의 __name__ 출력하기")
print(__name__)
print()
# %%
