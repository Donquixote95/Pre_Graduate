# %%
books = [{
    "제목" : "GSDS 입문",
    "가격" : 18000
}, {
    "제목" : "묵향",
    "가격" : 11000
}, {
    "제목" : "언제나 밤인 세계",
    "가격" : 24000
}]

def 가격추출함수(book):
    return book["가격"]

min(books, key=가격추출함수)
min(books, key=lambda book: book["가격"])

# 위 코드의 두 가지 문제
# (1) 콜백 함수 활용 ; 코드를 위에서 아래로 읽어 내리다가 '가격추출함수'가 무엇인지 알기 위해 함수를 찾아서 내용을 살펴봐야 한다.
# (2) 람다를 활용한 경우 ; 람다는 파이썬에만 있는 문법이기 때문에 다른 사람이 코드를 읽을 때 이해하지 못할 수도 있다.

# operator 모듈의 itemgetter() 함수를 활용해서 문제 해결

# %%
from operator import itemgetter
books = [{
    "제목" : "GSDS 입문",
    "가격" : 18000
}, {
    "제목" : "묵향",
    "가격" : 11000
}, {
    "제목" : "언제나 밤인 세계",
    "가격" : 24000
}]

print("# 가장 저렴한 책")
print(min(books, key=itemgetter("가격")))
print("----")

print("# 가장 비싼 책")
print(max(books, key=itemgetter("가격")))