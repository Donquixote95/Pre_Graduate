# inheritance
# multiple inheritance
# parent, child

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")
    
# 자식 클래스를 선언
class Child(Parent):
    def __init__(self):
        super().__init__() #부모의 __init__() 함수를 호출
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

# 자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출합니다.
child = Child()
child.test()
print(child.value)

# %%
# 상속 활용 - 예외 클래스 만들기
# Exception 이라는 기존의 클래스를 수정해서 CusmtomException 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        super().__init__()

raise CustomException

#%%
# Overide(오버라이드) ; 자식 클래스에서 부모의 함수 재정의

class CustomException(Exception):
    def __init__(self):
        super().__init__()
        print("#내가 만든 오류 생성#")
    def __str__(self): # Exception Class(부모 클래스)에도 정의된 함수
        return "오류가 발생"

raise CustomException
# %%
# 자식 클래스에서 부모에 없는 새로운 함수 정의
class CustomException(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message = message
        self.value = value

    def __str__(self): 
        return self.message
    
    def print(self):
        print("#오류 정보#")
        print("메시지:", self.message)
        print("값:", self.value)

# 예외를 발생
try:
    raise CustomException("No Reason", 273)
except CustomException as e:
    e.print()

# %%
