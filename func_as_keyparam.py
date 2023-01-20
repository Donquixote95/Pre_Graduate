# 키워드 매개변수에 함수 전달하기
# max(), min() 함수에는 '어떤 값으로 비교'할 것인지 나타내는 key라는 키워드 매개변수를 지정할 수 있다.

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

def price_assume(book):
    return book["가격"] # 딕셔너리에서 '가격' 값을 추출하는 함수를 선언

print("# book which has the most reasonable price.")
print(min(books, key = price_assume)) # 가격 값을 비교해서 최솟값을 구한다.
print()

print("# book which has the most expensive prce.")
print(max(books, key = price_assume))
print()

# 콜백 함수를 람다로 바꿀 수 있다.
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
print(min(books, key = lambda book: book["가격"]))

print("# 가장 비싼 책")
print(max(books, key = lambda book: book["가격"]))