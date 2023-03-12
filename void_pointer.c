// void pointer
// 주소는 가리키는 자료형이 일치하는 포인터에만 대입이 가능하다. 따라서 가리키는 자료형이 다른 주소를 저장하는 경우라면 void 포인터를 사용한다.
// void pointer는 가리키는 자료형이 정해지지 않은 포인터이다.
// void는 가리키는 자료형을 결정하지 않겠다는 뜻이다.
// void pointer는 어떤 주소든 저장할 수 있지만, 간접 참조 연산이나 정수를 더하는 포인터 연산이 불가능하다. 원하는 형태로 변환해서 사용해야 한다.
// 항 변환 연산자와 간접 참조 연산자는 모두 단항 연산자로서 우선순위가 같다.
#include <stdio.h>

int main(void)
{
    int a = 10;
    double b = 3.5;
    void *vp;

    vp = &a;
    printf("a : %d\n", *(int *)vp);

    vp = &b;
    printf("b : %.1lf\n", *(double *)vp);

    printf("a의 주소 : %d\na의 주소 + 1의 값 : %d\n", (int *)vp, (int *)vp + 1);

    //void 포인터가 형 변환을 하지 않는 경우는 대입 연산을 할 때이다. 형 변환 없이 void 포인터를 다른 포인터에 대입할 수 있다.
    int *pi2 = (int *)vp;
    int *pi1 = vp;

    return 0;
}

// 함수 포인터의 활용
// #include <stdio.h>

// void func(int (*fp)(int, int));
// int sum(int a, int b);
// int mul(int a, int b);
// int max(int a, int b);

// int main(void)
// {
//     int sel;    // 선택된 메뉴 번호를 저장할 변수

//     printf("01 두 정수의 합\n");
//     printf("02 두 정수의 곱\n");
//     printf("01 두 정수 중 더 큰 값\n");
//     printf("원하는 연산을 선택하라 : ");
//     scanf("%d", &sel); // 메뉴 번호 입력

//     switch (sel)
//     {
//     case 1: func(sum); break; //1을 선택하면 func에 덧셈 기능 추가
//     case 2: func(mul); break;
//     case 3: func(mul); break;
//     default:
//         break;
//     }

//     return 0;
// }

// void func(int (*fp)(int, int))
// {
//     int a, b;
//     int res;

//     printf("두 정수의 값을 입력하세요 : ");
//     scanf("%d%d", &a, &b);
//     res = fp(a, b);
//     printf("결괏값은 : %d\n", res);
// }

// int sum(int a, int b)
// {
//     return (a + b);
// }

// int mul(int a, int b)
// {
//     return (a * b);
// }

// int max(int a, int b)
// {
//     if (a > b) return a;
//     else return b;
// }
// 함수 포인터
// 함수명 : 함수 정의가 있는 메모리의 시작 위치, 즉 주소이다.

// 함수 포인터를 사용한 함수 호출

// #include <stdio.h>

// int sum(int, int);

// int main(void)
// {
//     int (*fp)(int, int); //function pointer
//     // 괄호가 없으면, int *fp(int, int); 로 선언하면, 두 정수를 인수로 받고 주소를 반환하는 함수의 선언이 된다. 포인터 선언이 아니게 된다.
//     int res;
//     int res1;
//     int res2;

//     fp = sum;
//     res = fp(10, 20);
//     res1 = (*sum)(10, 20);
//     res2 = sum(10, 20);
//     printf("result : %d\n", res);
//     printf("result1 : %d\n", res1);
//     printf("result2 : %d\n", res2);

//     return 0;
// }

// int sum(int a, int b)
// {
//     return (a + b);
// }