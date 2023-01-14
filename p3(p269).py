# 3. 염기 코돈 개수 세기
# 염기 서열은 일반적으로 3개씩 묶여서 하나의 의미를 나타낸다.

# 조건 1. 염기서열의 마지막이 3개로 조합되지 못하면 해당 부분은 무시한다.

codon = {}
option_key = ["cta", "caa", "tgt", "cag", "tat", "acc", "cat", "tgc", "att", "agc", "cgg"] # codon

blue_print = input("dna_blue_print>")
# ex_put; ctacaatgtcagtatacccattgcattagccgg
# ex_put2; ctacaatgtcagtatacccattgcattagccggc
# ex_put3; ctacaatgtcagtatacccattgcattagccggca

if len(blue_print) % 3 == 1:
    blue_print = blue_print[0 : (len(blue_print)-1)]
    for key in option_key:
        codon[key] = blue_print.count(key)
elif len(blue_print) % 3 == 2:
    blue_print = blue_print[0 : (len(blue_print)-2)]
    for key in option_key:
        codon[key] = blue_print.count(key)
else:
    for key in option_key:
        codon[key] = blue_print.count(key)
print(codon)

# print(len(blue_print))
# print("len(blue_print)".isdigit()) #False 놀랍게도..
# print("int(len(blue_print))".isdecimal())