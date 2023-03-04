// 하나의 문자열을 저장하기 위해서는 1차원 char 배열이 필요하고, 여러 개의 문자열을 저장하려면 1차원 char 배열이 여러개 필요하다.

#include <stdio.h>

int main(void)
{
    char animal[5][20];
    char animal1[5][10] = {
        {'d', 'o', 'g', '\0'},
        {'t', 'i', 'g', 'e', 'r', '\0'},
        {'r', 'a', 'b', 'b', 'i', 't', '\0'},
        {'h', 'o', 'r', 's', 'e', '\0'},
        {'c', 'a', 't', '\0'}
    };
    char animal2[][10] = { "dog", "tiger", "rabbit", "horse", "cat" }; //초기화하는 문자열 상수의 개수가 행의 수가 된다.
    //남는 char 저장 공간은 널 문자(\0)으로 채워진다.

    //3차원 배열
    int score[2][3][4] = {
        { {72, 80, 95, 60}, {68, 98, 83, 90}, {75, 72, 84, 90} },
        { {66, 85, 90, 88}, {95, 92, 88, 95}, {43, 72, 56, 75} }
    };

    int i, j, k;

    for (i = 0; i < 2; i++)
    {
        printf("%d반 점수...\n", i + 1);
        for (j = 0 ; j < 3; j++)
        {
            for (k = 0; k < 4; k++)
            {
                printf("%5d", score[i][j][k]);
            }
            printf("\n"); // 한 학생의 점수를 출력하고 줄 바꿈
        }
        printf("\n"); // 한 반의 점수를 출력하고 줄 바꿈
    }

    // int i;
    // int count;

    // for (i = 0; i < 5; i++)
    // {
    //     printf("%s ", animal1[i]);
    // }
    // printf("\n");

    // for (i = 0; i < 5; i++)
    // {
    //     printf("%s ", animal2[i]);
    // }

    // count = sizeof(animal) / sizeof(animal[0]);
    // for (i = 0; i < count; i++)
    // {
    //     scanf("%s", animal[i]);
    // }

    // for (i = 0; i < count; i++)
    // {
    //     printf("%s", animal[i]);
    //     printf("\t");
    // }

    return 0;
}