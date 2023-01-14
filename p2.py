# 2. 염기의 개수 세기
# DNA는 A(아데닌), T(티민), G(구아닌), C(사이토신) 4가지 요소로 이루어진다.

# 내 풀이
"""
blue_print = input("dna_blue_print>")

a_blue = blue_print.count("a")
t_blue = blue_print.count("t")
g_blue = blue_print.count("g")
c_blue = blue_print.count("c")

print("a의 개수:", a_blue)
print("t의 개수:", t_blue)
print("g의 개수:", g_blue)
print("c의 개수:", c_blue)
"""

# 답지 풀이
nucleos = input("염기 서열을 입력해주세요: ")
#ex input ; ctacaatgtcagtatacccattgcattagccgg
counter = {
    "a" : 0,
    "t" : 0,
    "g" : 0,
    "c" : 0
}

for nucleo in nucleos:
    counter[nucleo] += 1

for key in counter:
    print(f"{key}의 개수: {counter[key]}")