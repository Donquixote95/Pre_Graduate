#include <stdio.h>

int main(void)
{
    // 'X'자 별표 해설지 답
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if((i == j) || (i +j == 4))
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;

    // 'X'자 별표 모양을 만드는 법 (내가 만든 답)
    // int i, j;
    // for (i = 0; i < 5; i++)
    // {
    //     for (j = 0; j < 5; j++)
    //     {
    //         if (i==j)
    //         {
    //             printf("*");
    //         }
    //         else if ((i+j)==4)
    //         {
    //             printf("*");
    //         }
    //         else
    //         {
    //             printf(" ");
    //         }
    //     }
    //     printf("\n");
    // }

    //무한 반복문
    // while (1)
    // for (;;)

    // int count = 0;
    // int count2 = 0;
    // int i;
    
    // while(1)
    // {
    //     printf("Be happy!\n");
    //     count++;
    //     if (count == 5) break;
    // }
    
    // for (;;)
    // {
    //     printf("I love you!\n");
    //     count2++;
    //     if (count2 == 5) break;
    // }

    // for (i = 1; i <= 100; i++)
    // {
    //     if ((i % 3) == 0)
    //     {
    //         continue;
    //     }
    //     sum += i;
    // }

    // int i;
    // int sum = 0;

    // for (i=1; i <= 10; i++)
    // {
    //     sum += i;
    //     if (sum > 30) break; 
    //     //break는 자신을 포함하는 반복문 하나만 벗어난다. 반복문이 중첩된 경우 가장 안쪽에서 break를 사용해서 바깥쪽 반복문을 벗어날 수는 없다.
    //     //break는 반복문 이외의 블록에서 사용하면 그 블록을 포함한 반복문을 벗어난다.
    //     //그러나 if문과 달리 switch ~ case 블록 안에서 break를 사용하면 switch ~ case 블록만 벗어난다.
    // }
    // printf("accumulated sum : %d\n", sum);
    // printf("last i : %d\n", i);

    // return 0;
    
    // 구구단 출력
    // int i, j;
    // for (i = 2; i <= 9; i++)
    // {
    //     for (j = 1; j < 9; j++)
    //     {
    //     printf("%d * %d = %d\n", i, j, i*j);
    //     }
    // }
    // int i, j;

    // for (i=0; i < 3; i++)
    // {
    //     for (j = 0; j < 5; j++)
    //     {
    //         printf("*");
    //     }
    //     printf("\n");
    // }

    // return 0;

    // int a = 1;

    // do
    // {
    //     a = a *2;
    // }while(a < 10);
    // printf("a : %d\n", a);

    // return 0;

    // int a =1;
    // int i;

    // for (i = 0; i < 3; i++)
    // {
    //     a = a*2;
    // }
    // printf("a : %d\n", a);

    // return 0;
    
    // int a = 1;

    // while (a < 10)
    // {
    //     a = a *2;
    // }
    // printf("a : %d\n", a);

    // return 0;
}