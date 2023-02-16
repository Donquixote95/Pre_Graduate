#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int a;

    scanf("%d", &a); //scan formatted
    printf("입력된 값 : %d\n", a);

    int age;
    double height;

    printf("나이와 키를 입력하세요 : ");
    scanf("%d%lf", &age, &height);
    printf("나이는 %d살, 키는 %.1lfcm입니다.\n", age, height);

    char grade;
    char name[20];

    printf("학점 입력 : ");
    scanf("%c", &grade);

    printf("이름 입력 : ");
    scanf("%s", name);

    printf("%s의 학점은 %c입니다.\n", name, grade);

    return 0;
}

/*
정수 (unsigned) 2byte %hd(%hu)
정수 (unsigned) 4byte %d(%u)
정수 (unsigned) 4byte %ld(%lu)
정수 (unsigned) 8byte %lld(%llu)

실수 float 4byte %f
실수 double 8byte %lf
실수 long double 8, 10, 12, 16byte $Lf

문자 char 1byte $c

문자열 char 배열 가변적 $s
*/