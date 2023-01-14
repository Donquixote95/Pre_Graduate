# n 진수 → 10 진수
# int(string, base)

"""
2진수 : 0b(binary number) ; bin
8진수 : 0o(octal number) ; oct
10진수 : decimal
16진수 : 0x(hexadecimal number) ; hex
"""
#16진법은, (10진법 표기 : 16진법 표기) ;  10:A, 11:B, 12:C, 13:D, 14:E, 15:F

#10진수와 2진수 변환
print("{:b}".format(10)) #bi를 줄였기 때문에 :b
print(int("1010", 2))
print()

#10진수와 8진수의 변환
print("{:o}".format(10)) #oct를 줄였기 때문에 :o
print(int("12", 8))
print()

#10진수와 16진수의 변환
print("{:x}".format(10)) #hexa를 줄였기 때문에 :x
print(int("12", 16))
print()

#iterable(반복 가능한) 객체의 count() 함수는 다음과 같이 사용한다.
print("HelloHelloHelllo".count("Hello"))

# 1~100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드

output = [i for i in range(1, 100+1) if "{:b}".format(i).count("0")==1]

for i in output:
    print("{}:{}".format(i, "{:b}".format(i)))
print("sum_output:", sum(output))