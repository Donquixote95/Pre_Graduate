PI = 3.141592

def number_input():
    output = input("integer> ")
    return float(output)

def get_circumference(radius):
    return 2* PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# __name__ 활용하기
# 활용 예
if __name__ == "__main__": # 현재 파일이 엔트리 포인트인지 확인하고, 엔트리 포인트일 때만 실행한다.
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))