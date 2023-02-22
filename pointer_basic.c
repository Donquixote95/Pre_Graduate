#include <stdio.h>

//const를 사용한 포인터

int main(void)
{
    int a = 10, b = 20;
    const int *pa = &a;

    printf("value of a : %d\n", *pa);
    pa = &b;
    printf("value of b : %d\n", *pa);
    pa = &a;
    a = 20;
    printf("value of a : %d\n", *pa);

    return 0;
    // int a = 10, b = 15, total;
    // double avg;
    // int *pa, *pb;
    // int *pt = &total;
    // double *pg = &avg;

    // pa = &a;
    // pb = &b;

    // *pt = *pa + *pb;
    // *pg = *pt / 2.0;

    // printf("the value of two integers : %d, %d\n", *pa, *pb);
    // printf("sum of two integer : %d\n", *pt);
    // printf("the average of two integers : %.1lf\n", *pg);

    // return 0;


    // int a;
    // int *pa;

    // pa = &a;
    // *pa = 10;

    // printf("pointer of a : %d\n", *pa);
    // printf("a : %d\n", a);

    // return 0;

    //주소는 보통 16진수로 표기한다. 주소를 출력할 떄는 전용 변환 문자인 %p를 사용하는 것이 좋다.
    //%p는 주소값의 데이터 크기에 따라 자릿수를 맞춰 16진수 대문자로 출력한다
    //시스템에서 주소값 자체를 4바이트로 처리한다면 16진수 한 자리는 4비트에 해당하므로 주소값 10은 0000000A와 같이 16진수 8자리로 출력한다.
    //1byte = 8bit

    // int a;
    // double b;
    // char c;

    // printf("int형 변수의 주소 : %d\n", &a);
    // printf("int형 변수의 주소 : %p\n", &a);
    // printf("double형 변수의 주소 : %d\n", &b);
    // printf("double형 변수의 주소 : %p\n", &b);
    // printf("char형 변수의 주소 : %d\n", &c);
    // printf("char형 변수의 주소 : %p\n", &c);

    // return 0;
}