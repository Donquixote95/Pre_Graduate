//2차원 배열의 값을 출력하는 함수
#include <stdio.h>

void print_ary(int (*)[4]);

int main(void)
{
    int ary[3][4] = { {1,2,3,4}, {5,6,7,8}, {9,10,11,12} };

    print_ary(ary); //배열명을 인수로 주고 함수 호출

    return 0;
}

void print_ary(int (*pa)[4]) //매개변수는 배열 포인터
{
    int i, j;

    for (i=0; i<3; i++)
    {
        for (j=0; j<4; j++)
        {
            printf("%5d", pa[i][j]);
        }
        printf("\n");
    }
}

//2차원 배열과 배열 포인터
// #include <stdio.h>

// int main(void)
// {
//     int ary[3][4] = { {1,2,3,4}, {5,6,7,8}, {9,10,11,12} };
//     int (*pa)[4]; //int형 변수 4개의 배열을 가리키는 배열 포인터, int 4개의 1차원 배열을 가리킨다. 괄호가 없으면 포인터 배열이 된다. *pa이기 때문에 pa는 포인터다.
//     int i, j;

//     pa = ary; // 포인터에 배열명을 저장하면 배열처럼 쓸 수 있다. 
//     for (i = 0; i < 3; i++)
//     {
//         for (j = 0; j < 4; j++)
//         {
//             printf("%5d", pa[i][j]); // 포인터에 배열명을 저장했기 때문에 배열 포인터를 2차원 배열처럼 쓸 수 있다.
//         }
//         printf("\n");
//     }

//     return 0;
// }

//주소로 쓰이는 배열명과 배열의 주소 비교
// #include <stdio.h>

// int main(void)
// {
//     int ary[5];

//     printf(" ary의 값 : %u\t", ary);
//     printf("ary의 주소 : %u\n", &ary);
//     printf("  ary + 1 : %u\t", ary + 1);
//     printf(" &ary + 1의 주소 : %u\n", &ary + 1);

    // ary 자체가 주소로 쓰일 때는 첫 번째 요소를 가리킨다.
    // &ary는 배열의 주소로서, 배열 전체를 가리킨다. 

    /*
    위 경우,
    배열의 정수 연산인
    ary + 1은 기존 주소 + 1 * sizeof(ary[0]) 이지만,

    배열의 주소에 정수 연산을 하는
    &ary + 1은 기존 주소 + 1 * sizeof(ary)가 된다.

    sizeof(ary)와 sizeof(ary[0])은 당연히 다르다. 
    */

//     return 0;
// }

//다중 포인터
//3중 포인터의 선언 예시 double ***ppp;

// 이중 포인터의 활용 1; 포인터 값을 바꾸는 함수의 매개변수
// 이중 포인터의 활용 2; 포인터 배열을 매개변수로 받는 함수
// #include <stdio.h>

// void swap_ptr(char **ppa, char **ppb);
// void print_str(char **pps, int cnt);

// int main(void)
// {
//     char *ptr_ary[] = {"eagle", "tiger", "lion", "squirrl"}; 
//     int count; //배열 요소 수를 저장할 변수

//     count = sizeof(ptr_ary) / sizeof(ptr_ary[0]); // 배열 요소 수 계산
//     print_str(ptr_ary, count); //배열명과 배열 요소 수를 주고 호출

//     char *pa = "success";
//     char *pb = "failure";

//     printf("pa -> %s, pb -> %s\n", pa, pb);
//     swap_ptr(&pa, &pb);
//     printf("pa -> %s, pb -> %s\n", pa, pb);

//     return 0;
// }

// void swap_ptr(char **ppa, char **ppb)
// {
//     char *pt;

//     pt = *ppa;
//     *ppa = *ppb;
//     *ppb = pt;
// }

// void print_str(char **pps, int cnt)
// {
//     int i;

//     for (i = 0; i < cnt; i++)
//     {
//         printf("%s\n", pps[i]);
//     }
// }

// 포인터도 메모리에 저장 공간을 갖는 하나의 변수이므로 주소 연산으로 포인터의 주소도 구할 수 있다.

// #include <stdio.h>

// int main(void)
// {
//     int a =10; //int형 변수의 선언과 초기화
//     int *pi;   //pointer 선언
//     int **ppi; //이중 pointer 선언

//     pi = &a;    //int형 변수의 주소를 저장한 포인터
//     ppi = &pi;  //포인터의 주소를 저장한 이중 포인터

//     printf("-------------------------------------------\n");
//     printf("변수    변숫값     &연산     *연산   **연산\n");
//     printf("-------------------------------------------\n");
//     printf("  a%10d%10u\n", a, &a);
//     printf(" pi%10u%10u%10d\n", pi, &pi, *pi);
//     printf("ppi%10u%10u%10u%10u\n", ppi, &ppi, *ppi, **ppi);
//     printf("-------------------------------------------\n");

//     return 0;
// }