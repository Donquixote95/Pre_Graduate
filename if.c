#include <stdio.h>

int main(void)
{
    //switch ~ case
    //rule1. 조건식은 정수식만 사용한다.
    //rule2. case는 break를 포함한다. break를 생략할 수도 있지만 블록의 끝까지 문장을 실행한다.

    int rank = 2, m =0;

    switch (rank)
    {
        case 1:
            m = 300;
            break;
        case 2:
            m = 200;
            break;
        case 3:
            m = 100;
            break;
        default:
            m = 10;
            break;
    }
    printf("m : %d\n", m);

    return 0;

    // int a = 0, b = 0;

    // if (a>0)
    // {
    //     b = 1;
    // }
    // else if (a ==0)
    // {
    //     b = 2;
    // }
    // else
    // {
    //     b = 3;
    // }

    // printf(" b = %d\n", b);
    return 0;
}