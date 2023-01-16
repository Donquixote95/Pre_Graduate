# 함수를 사용하면 가독성 향상에 도움이 된다.
# 주석은 필요한 경우에 정확하게 사용하면 가독성 향상에 좋다.

# code maintenance

print("<p>{}</p>".format("안녕하세요."))
print("<p>{}</p>".format("간단한 HTML 태그를 만드는 예입니다."))

# p 태그로 감싸는 함수
def p(content):
    # 기존 코드 주석 처리
    # return "<p>{}</p}".format(content)
    # 2022.03.02
    return "<p class = 'content-line'>{}<p>".format(content)

# 출력한다
print(p("안녕하세요."))
print(p("간단한 HTML 태그를 만드는 예입니다."))

# 모든 경우를 탐색하는 유형의 문제
"""
여러 개의 테이블에 나누어 앉으려고 한다.
한 사람만 앉는 테이블이 없게 조합한다.
한 개의 테이블에 앉을 수 있는 최대 사람 수는 10명이다. 
100명의 사람이 나누어 앉는 패턴을 구하라.
"""

# 메모화를 위한 딕셔너리 선언
memo = {}

# 전체 사람 수
all_people = 100

# 테이블에 앉을 수 있는 최소 사람 수
min_table = 2

# 테이블에 앉을 수 있는 최대 사람 수 
max_table = 10

# remainder : 남은 사람 수, sitted : 앉히는 사람 최소 단위
def pattern(remainder, sitted): 
    key = str([remainder, sitted])
    # 종료 조건
    if remainder == 0:
        return 1 # 유효하니 수를 세면 돼서 1을 리턴, 예를 들어 2명이 남았는데 2명을 앉히는 경우의 수임.
    if remainder < 0:
        return 0 # 유효하지 않은 값, 0을 리턴
    if key in memo:
        return memo[key]
    # 재귀 처리
    count = 0
    for i in range(sitted, max_table + 1):  # i는 사람을 앉히는 단위 역할, i가 2일 때는 2명씩 계속 앉히는 것, max_table로 앉히는 것까지 각각의 경우를 세는 것
        count += pattern(remainder - i, i)  # 퍼즐이라 생각했을 때, 그림을 완성하기 위해서 조각 하나하나를 모으는 과정. 
        """
        기본 아이디어는, 예를 들어, 5명을 2명 이상씩 앉힐 경우의 수를 구하려고 하면
        2명을 앉혔다고 가정하고 남은 사람 수를 앉히는 경우의 수 + 
        3명을 앉혔다고 가정하고 남은 사람 수를 앉히는 경우의 수 +
        4명을 앉혔다고 가정하고 남은 사람 수를 앉히는 경우의 수 +
        5명을 앉혔다고 가정하고 남은 사람 수를 앉히는 경우의 수 +
        위 반복을, 자명한 값(남은 사람이 n명인데 n명을 앉히는 경우의 수)을 기반으로 쌓아올리듯 반복한다.
        """
    # 메모화 처리
    memo[key] = count
    # 종료
    return count    

print(pattern(all_people, min_table))