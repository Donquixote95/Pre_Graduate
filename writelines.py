with open("test.txt", "w") as file:
    #writelines() 기본 사용
    file.writelines(["Hi.",\
            "line change",\
            "No?"\
            "spacebar?"])
    file.writelines([True, 273, "str"])