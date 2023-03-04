//값을 복사해서 전달하는 방법 call by value
//call by reference
//지역 변수(auto variablem, local variable)의 주소를 반환해서는 안 된다.
#include <stdio.h>

int *sum(int a, int b);

int main(void)
{
    int *resp; //반환값을 저장할 포인터 resp(result pointer)

    resp = sum(10, 20);
    printf("Sum of two integers : %d\n", *resp); //resp가 가리키는 변수값 출력

    return 0;
}

int *sum(int a, int b) //int형ㄹ 변수의 주소를 반환하는 함수
{
    static int res;

    res = a + b;

    return &res;
}

// void add_ten(int *pa);

// int main(void)
// {
//     int a = 10;

//     add_ten(&a);
//     printf("a : %d\n", a);

//     return 0;
// }

// void add_ten(int *pa)
// {
//     *pa += 10;
// }