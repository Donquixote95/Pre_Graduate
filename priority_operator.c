// 순서 : 단항 연산자 > 이항 연산자 > 삼항 연산자
// 순서 : 산술 연산자 > 비트 이동 연산자 > 관계 연산자 > 논리 연산자

#include <stdio.h>

int main(void)
{
    int a= 10, b = 5;
    int res;

    res = a / b * 2;
    printf("res = *d\n", res);

    res = ++a * 3;
    printf("res = %d\n", res);

    res = a > b && a != 5;
    printf("res = %d\n", res);

    res = a % 3 == 0;
    printf("res = %d\n", res);

    return 0 ;
}