numbers = [1,2,3,4,5,6]

print("::".join(map(str,numbers)))

# 위 코드에서 map 함수와 str 함수 없이 numbers를 넣으면
# TypeError: sequence item 0: expected str instance, int found 라는 오류가 발생한다.
# 문자열이 들어있을 것으로 예상했는데, 숫자가 들어있다는 의미
# 즉, 리스트 내부의 모든 숫자를 문자열로 변환해야 한다.

numbers = list(range(1, 10 + 1))

print("# Odd number filter")
print(list(filter(lambda x: x%2==1,numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3<=x<7,numbers)))
print()

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda x: x**2 < 50 , numbers)))
print()

# Rule 1. 한 번에 한 개의 원판만 옮길 수 있다.
# Rule 2. 큰 원판이 작은 원판 위에 있어서는 안 된다.
# Rule 3. 하노이 탑에는 3개의 기둥이 있다. 각각의 기둥을 A, B, C로 표현한다.

# '시작 기둥' ; 처음 원판이 있는 기둥
# '대상 기둥' ; 원판을 옮겨야 하는 기둥
# '보조 기둥' ; 보조적으로 활용하는 기둥 

# 원판의 개수가 n개일 때 2^n -1 회 움직여야 원판을 모두 옮길 수 있다.


# 연습
"""
if 원판이 1개:
    이동 from 시작기둥 to 대상 기둥

A탑 -> B탑
"""

"""
if 원판이 2개
 1. 위에 있는 원판을 '보조 기둥'으로 옮기고
 2. 아래에 있는 원판을 '대상 기둥'으로 옮긴 뒤
 3. '보조 기둥'에 있던 원판을 '대상 기둥'으로 옮기면
 4. 모든 원판이 '대상 기둥'으로 옮겨진다.
"""

"""
if 원판 하나와 원판 덩어리가 있다면, 원판을 시작기둥에서 대상기둥으로 옮기는 경우
 1. 덩어리를 보조 기둥으로 옮긴다
 2. 아래의 원판을 대상기둥으로 옮긴다.
 3. 보조 기둥에 있던 덩어리를 대상기둥으로 옮긴다.
 4. 모든 원판이 대상기둥으로 옮겨진다.
"""

"""
if 원판이 2개 이상
 1. 덩어리 이동 from 시작기둥 to 보조기둥
 2. 이동 from 시작기둥 to 대상기둥
 3. 덩어리 이동 from 보조기둥 to 대상기둥
이동 from 시작기둥 to 대상기둥
"""

# 하노이 탑에서 필요한 요소를 모두 매개변수로 받는다.

# (0) Memorization, initialization of global variables

# pillar_list = ["pillar_s", "pillar_e", "pillar_a"]
# memo = {}
# counter = 0

# # (1) 클래스 선언, initialization
# class HanoiTower:
#     def __init__(self, n : int, pillar_s : str, pillar_e : str, pillar_a : str) -> None:
#         self.n = n
#         self.pillar_s = pillar_s
#         self.pillar_e = pillar_e
#         self.pillar_a = pillar_a

# # (2) Method, initialization of local variables
#     def count(self) -> dict:
#         global memo # Final Result ; {key : n, value : HanoiTower(n).count()} 
#         global counter # Result of value ; HanoiTower(n).count() 
#         n = self.n # n is defined


# # (4) Algorithms ; Recursion
#         if n == 1:
#             counter += 1
#             print("From", self.pillar_s, "To", self.pillar_e)
#             memo[n] = counter

#         else:
#             # (4-1) 아래의 원판을 제외하고, 시작 기둥에서 보조 기둥으로 이동
#             n -= 1
#             HanoiTower(n, self.pillar_s, self.pillar_a, self.pillar_e).count()
#             print("From", self.pillar_s, "To", self.pillar_e)

#             # (4-2) 아래의 원판을 제외하고, 보조 기둥에서 대상 기둥으로 이동
#             n -= 1
#             HanoiTower(n, self.pillar_a, self.pillar_e, self.pillar_s).count()

#         #  # (6) End
#         # memo[n] = counter 
#         # return memo[n]
    
# HanoiTower(6,"A탑","B탑","C탑").count()

# 답안지
# (1) ; 임의의 n에 대해 어떻게 원판을 옮겨야 하는가
def 하노이탑(이동해야하는원판, 시작기둥, 대상기둥, 보조기둥):
    if 이동해야하는원판 == 1:
        print(시작기둥, "->", 대상기둥)
    else:
        하노이탑(이동해야하는원판-1, 시작기둥, 보조기둥, 대상기둥)
        print(시작기둥, "->", 대상기둥)
        하노이탑(이동해야하는원판-1, 보조기둥, 대상기둥, 시작기둥)

n = int(input("원판의 개수를 입력해주세요: "))
하노이탑(n, "A탑", "B탑", "C탑")

# (2) ; 하노이탑 이동 횟수
횟수 = 0
def 하노이탑(이동해야하는원판, 시작기둥, 대상기둥, 보조기둥):
    global 횟수
    if 이동해야하는원판 == 1:
        # print(시작기둥, "->", 대상기둥)
        횟수 += 1
    else:
        하노이탑(이동해야하는원판-1, 시작기둥, 보조기둥, 대상기둥)
        # print(시작기둥, "->", 대상기둥)
        하노이탑(이동해야하는원판-1, 보조기둥, 대상기둥, 시작기둥)
    
n = int(input("원판의 개수를 입력: "))
하노이탑(n, "A탑", "B탑", "C탑")
print(f"이동 횟수는 {횟수}회입니다.")