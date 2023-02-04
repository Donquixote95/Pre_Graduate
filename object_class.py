"""
class 클래스 이름:
    클래스 내용
"""

# 생성자(constructor) : 클래스 이름과 같은 함수

"""
인스턴스 이름(변수 이름) = 클래스 이름() # 생성자 함수라고 부른다.
"""

# instance(인스턴스) : 클래스를 기반으로 만들어진 객체

"""
class 클래스 이름:
    def __init__(self, 추가적인 매개변수):
        pass
"""

# 클래스 내부에 __init__라는 함수를 만들면 객체를 생성할 때 처리할 내용을 작성할 수 있다.

# 클래스 내부의 함수는 첫 번째 매개변수로 반드시 self를 입력해야 한다.
# self는 '자기 자신'을 나타내는 딕셔너리라고 생각하면 된다.
# 다만 self가 가지고 있는 속성과 기능에 접근할 떄는 self.<식별자> 형태로 접근한다.

# self ; 키워드가 아니라 단순한 식별자이므로 변수 이름으로 활용해도 된다. 하지만 거의 모든 파이썬 개발자가 self라는 이름을 사용하므로 기본 규칙을 지키는 게 좋다.

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("별빛", 87, 98, 88, 95),
    Student("달빛", 92, 98, 96, 98),
    Student("햇빛", 82, 89, 92, 93),
    Student("그늘", 99, 100, 87, 88),
    Student("바람", 81, 98, 77, 80),
    Student("노래", 88, 77, 66, 99)
]

# Student 인스턴스의 속성에 접근하는 방법
students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

# 소멸자(destructor): 인스턴스가 소멸될 때 호출되는 함수
# 소멸자는 클래스 내부에 __del__(self) 형태로 함수를 선언해서 만든다.
class Test:
    def __init__(self, name) -> None:
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))
    def __del__(self) -> None:
        print("{} - 파괴되었습니다.".format(self.name))

test = Test("A")
# 위 코드를 실행하면 Test("A")가 실행될 때 생성자가 호출되며, 프로그램이 종료될 때 소멸자가 호출된다.


# method(메소드) : 클래스가 가지고 있는 함수
"""
class 클래스 이름:
    def 메소드 이름(self, 추가적인 매개변수):
        pass
"""

# C#, Java 등의 프로그래밍 언어는 클래스의 함수를 '메소드'라고 부를 정도로 메소드라는 용어를 많이 사용한다.
# 파이썬 프로그래밍 언어에서는 멤버 함수(member function) 또는 인스턴스 함수(instance function) 등의 용어를 더 많이 사용한다.

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self) -> int:
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self) -> float:
        return self.get_sum() / 4
    
    def to_string(self) -> str:
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

# 학생 리스트를 선언
students = [
    Student("별빛", 87, 98, 88, 95),
    Student("달빛", 92, 98, 96, 98),
    Student("햇빛", 82, 89, 92, 93),
    Student("그늘", 99, 100, 87, 88),
    Student("바람", 81, 98, 77, 80),
    Student("노래", 88, 77, 66, 99)
]

# 학생을 한 명씩 반복한다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())


# 상속 ; 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 것

# isinstance() 함수 ; 상속 관계에 따라서 객체가 어떤 클래스를 기반으로 만들었는지 확인하는 함수
"""
isinstance(인스턴스, 클래스)
# 인스턴스가 해당 클래스를 기반으로 만들어졌으면 True, 아니면 False
"""

print("isinstance(student, Student):", isinstance(student, Student))

# 단순한 인스턴스 확인
# type(인스턴스) == 클래스
# 단, 위 방법은 상속을 사용할 때 다르게 동작한다.
print(type(student) == Student)

class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass

student = Student()

print("isinstance(student, Human):", isinstance(student, Human))
print("type(student)==Human:", type(student) == Human)

# isinstance() 함수 활용
class Student:
    def study(self):
        print("do study!")
class Teacher:
    def teach(self):
        print("do teach!")
classroom = [Student(), Student(), Teacher(), Student(), Student()]
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

# 특수한 이름의 메소드
# str 함수 ; 파이썬이 기본적으로 제공하는 함수. 
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self) -> int:
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self) -> float:
        return self.get_sum() / 4
    
    def __str__(self) -> str:
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    
students = [
    Student("별빛", 87, 98, 88, 95),
    Student("달빛", 92, 98, 96, 98),
    Student("햇빛", 82, 89, 92, 93),
    Student("그늘", 99, 100, 87, 88),
    Student("바람", 81, 98, 77, 80),
    Student("노래", 88, 77, 66, 99)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student)) #str() 함수의 매개변수로 넣으면 studnet의 __str__() 함수가 호출된다.


"""
이름    영어                    설명
eq      equal                   같다
ne      not equal               다르다
gt      greater than            크다
ge      greater than or equal   크거나 같다
lt      less than               작다
le      less than or equal      작거나 같다
"""

# 크기 비교 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self) -> int:
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self) -> float:
        return self.get_sum() / 4
    
    def __str__(self) -> str:
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
    
students = [
    Student("별빛", 87, 98, 88, 95),
    Student("달빛", 92, 98, 96, 98),
    Student("햇빛", 82, 89, 92, 93),
    Student("그늘", 99, 100, 87, 88),
    Student("바람", 81, 98, 77, 80),
    Student("노래", 88, 77, 66, 99)
]

# 학생 선언
studnet_a = Student("별빛", 87, 98, 88, 95)
studnet_b = Student("달빛", 92, 98, 96, 98)

# 출력
print("studnet_a == studnet_b: ", studnet_a == studnet_b)
print("studnet_a != studnet_b: ", studnet_a != studnet_b)
print("studnet_a > studnet_b: ", studnet_a > studnet_b)
print("studnet_a >= studnet_b: ", studnet_a >= studnet_b)
print("studnet_a < studnet_b: ", studnet_a < studnet_b)
print("studnet_a <= studnet_b: ", studnet_a <= studnet_b)

# 예외 처리
# ==, !=, >, >=, <, <= 를 사용하면 곧바로 함수가 호출된다. 이는 서로 다른 자료형을 비교할 때도 마찬가지다.
# 만약 비교할 때 사용되는 자료형을 한정하고 싶다면, 자료형을 한정하고 이외의 자료형을 사용할 때 예외를 발생시키면 된다.

# 일반적으로 문자열과 숫자를 비교하면 TypeError가 발생한다.
# '비교할 수 없는 자료형을 비교할 때 TypeError를 발생시키는 것'은 파이썬의 기본 동작이다. 이를 지켜 클래스를 구현하면 된다.
# TypeError 발생시키기 - isinstance() 함수를 활용하는 방법
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science    
    # 생략
    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있다.")
        return self.get_sum() == value.get_sum()
    # 생략
# 학생 선언
studnet_a = Student("별빛", 87, 98, 88, 95)
# 비교
studnet_a == 10

# %%
# 인스턴스가 속성과 기능을 가질 수도 있지만, 클래스가 속성(변수)와 기능(함수)을 가질 수도 있다.
# 클래스 변수
"""
클래스 변수 만들기
class 클래스 이름:
    클래스 변수 = 값

클래스 변수에 접근하기
클래스 이름.변수 이름
"""

class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science    

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

# 학생 리스트 선언
students = [
    Student("별빛", 87, 98, 88, 95),
    Student("달빛", 92, 98, 96, 98),
    Student("햇빛", 82, 89, 92, 93),
    Student("그늘", 99, 100, 87, 88),
    Student("바람", 81, 98, 77, 80),
    Student("노래", 88, 77, 66, 99)
]

# 출력
print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))
# 클래스 내부와 외부에서 클래스 변수에 접근할 때는 모두 Studnet.count 형태(클래스 이름, 변수 이름)을 사용한다.

# %%
# 클래스 함수 ; 클래스가 가진 함수
"""
class 클래스 이름:
    @classmethod
    def 클래스 함수(cls, 매개변수): #cls 대신 원하는 이름을 사용해도 되지만, 관례적으로 cls를 사용한다.
        pass
"""
# 클래스 데코레이터; @로 시작하는 것을 파이썬에서는 '데코레이터'라고 하며 '꾸며 주는 것'이라는 의미를 가진다.
# 데코레이터는 만드는 방법에 따라 함수 데코레이터, 클래스 데코레이터로 나뉜다.

# 클래스 함수의 첫 번째 매개변수에는 클래스 자체가 들어온다. 일반적으로 cls('클래스'라고 읽는다.)라는 이름의 변수로 선언하며 다음과 같이 사용한다.
# 클래스 함수 호출하기
"""
클래스 이름.함수 이름(매개변수)
"""

class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls): #studnet 클래스에 print() 함수를 구현
        print("------학생 목록------")
        print("이름\t총점\t평균")
        for student in cls.students: #studnet.students라고 해도 되지만, 매개변수로 받은 cls 를 활용한다.
            print(str(student))
        print("------ ------ ------")


    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science  
        Student.count += 1
        Student.students.append(self)

    def get_sum(self) -> int:
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self) -> float:
        return self.get_sum() / 4
    
    def __str__(self) -> str:
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

# 학생 리스트를 선언
Student("별빛", 87, 98, 88, 95),
Student("달빛", 92, 98, 96, 98),
Student("햇빛", 82, 89, 92, 93),
Student("그늘", 99, 100, 87, 88),
Student("바람", 81, 98, 77, 80),
Student("노래", 88, 77, 66, 99)    

Student.print()
# %%
# garbage collector(가비지 컬렉터) 
# - 더 사용할 가능성이 없는 데이터를 메모리에서 제거하는 역할
# - 변수에 저장되지 않거나, 함수 등에서 나오면서 변수를 활용할 수 없게 되는 경우

# swap ;  메모리가 부족해지면 하드디스크를 메모리처럼 사용해서 무언가를 올리는 것

# 가비지 컬렉터: 변수에 저장하지 않은 경우
# - A가 생성되고 다음 줄로 넘어갈 때 이것을 변수에 저장하지 않으면 가비지 컬렉터는 이후에 활용하지 않겠다는 의미로 이해하고 메모리를 아끼기 위해 지운다.

# 가비지 컬렉터: 변수에 저장한 경우
# - 변수에 저장했으면 나중에 활용할 가능성이 있으므로 프로그램이 종료되는 순간까지 가비지 컬렉터가 데이터를 메모리에서 제거하지 않는다.
# 따라서 A생성, B생성, C생성 이후에 프로그램이 종료될 때 A파괴, B파괴, C파괴가 일어난다.