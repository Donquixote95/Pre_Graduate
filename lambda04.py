a = [52, 273, 103, 32, 57, 272]
a.sort()
print(a)
print()
# a는 파괴적 함수이기 떄문에 호출했을 때 리스트 자체가 바뀐다.

# 기본 오름차순 정렬이므로 내림차순 정렬을 하고 싶다면 reverse 키워드 매개변수를 True로 지정한다

a.sort(reverse=True)
print(a)

# Dictionary의 List를 정렬하려면 딕셔너리의 키를 활용하여 key 키워드 매개변수에 람다를 사용하면 된다.

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

print("# 가격 오름차순 정렬")
books.sort(key = lambda book: book["가격"])
for book in books: # sort는 파괴적 함수이므로 books 내 값을 추출하면 정렬된 모습을 확인할 수 있다.
    print(book)


# 매개변수가 여러 개인 람다도 만들 수 있다.
# lambda x, y: x * y