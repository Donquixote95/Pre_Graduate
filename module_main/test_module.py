#test_module.py 파일
PI = 3.141592

def number_input():
    output = input("integer> ")
    return float(output)

def get_circumference(radius):
    return 2* PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# __name__=="__main__"

# __name__ ; pyhton 코드 내부에서는 __name__ 변수를 사용할 수 있다.
# 프로그래밍 언어에서는 프로그램의 진입점을 entry point(엔트리 포인트), 메인(main)이라고 부른다.
# 엔트리 포인트 또는 메인 내부에서의 __name__은 "__main__"이다.

# %%
# 모듈 이름을 출력하는 모듈 만들기
print("# 모듈의 __name__ 출력하기")
print(__name__)
print()

# %%