#include <stdio.h>
void print_ary(int *pa, int size);

int main(void)
{
    //배열의 값을 출력하는 함수    
    int ary1[5] = {10, 20 , 30 ,40 ,50};
    int ary2[7] = {10, 20 , 30 ,40 ,50, 60, 70};
    print_ary(ary1, sizeof(ary1) / sizeof(ary1[0]));
    printf("\n");
    print_ary(ary2, 7);

    return 0;

    //pointer abstraction
    // pointer - pointer = difference of values / size of data structure

    // int ary[5] = {10, 20, 30, 40, 50};
    // int *pa = ary;
    // int *pb = pa +3;

    // printf("pa : %u\n",pa);
    // printf("pb : %u\n",pb);
    // pa++;
    // printf("pb-pa : %u\n",pb-pa);

    // printf("앞에 있는 배열 요소의 값 출력 : ");
    // if (pa < pb)
    // {
    //     printf("%d\n", *pa);
    // }
    // else{
    //     printf("%d\n", *pb);
    // }
    // return 0;
    
    //포인터를 이용한 배열의 값 출력
    // int ary[3] = {10, 20, 30};
    // int *pa = ary;
    // int i;

    // printf("the value of array : \n");
    // for (i = 0; i < 3; i++)
    // {
    //     printf("%d\n", *(pa++));
    // }

    // for (i = 0; i < 3; i++)
    // {
    //     printf("%d\n", *pa);
    //     pa++;
    // }

    // return 0;

    //배열명과 포인터의 차이
    // sizeof 연산자의 결과가 다르다.
    // 포인터는 그 값을 바꿀 수 있지만, 배열명은 상수이므로 값을 바꿀 수 없다.
    // int ary[3];
    // int *pa = ary;
    // printf("%d\n", sizeof(ary));
    // printf("%d\n",sizeof(pa));


    //배열명처럼 사용하는 포인터
    // int ary[3];
    // int *pa = ary;
    // int i;

    // *pa = 10;
    // *(pa + 1) = 20;
    // pa[2] = pa[0] + pa[1];

    // for (i = 0; i < 3; i++)
    // {
    //     printf("%5d", pa[i]);
    // }

    // return 0;

    // int ary[3];
    // int i;

    // *(ary + 0) = 10;
    // *(ary + 1) = *(ary + 0) + 10;

    // printf("third element : ");
    // scanf("%d", ary + 2); //scdanf("%d", &ary[2]); 와 같다.

    // for (i = 0; i < 3; i++)
    // {
    //     printf("%5d", *(ary + i));
    // }

    // return 0;
}

void print_ary(int *pa, int size)
{
    int i;

    for (i=0; i < size; i++)
    {
        printf("%d\n", pa[i]);
    }
}