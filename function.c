//recursive call function
#include <stdio.h>

void fruit(int count );

int main(void)
{
    fruit(1);

    return 0;
}

void fruit(int count)
{
    printf("apple\n");
    if (count == 3)
    {
        return;
    }
    fruit(count + 1);
    printf("jam\n");
}

// 매개변수와 반환값이 모두 없는 함수

// #include <stdio.h>
// void print_line(void);

// int main(void)
// {
//     print_line();
//     printf("Student_num  name  major  grade\n");
//     print_line();

//     return 0;
// }

// void print_line(void)
// {
//     int i;
//     for (i=0; i<50; i++)
//     {
//         printf("-");
//     }
//     printf("\n");
// }

// 반환값이 없는 함수는 반환형 자리에 void를 사용한다.

// #include <stdio.h>

// void print_char(char ch, int count);

// int main(void)
// {
//     print_char('@', 5);

//     return 0;
// }

// void print_char(char ch, int count)
// {
//     int i;

//     for (i=0; i <count; i++)
//     {
//         printf("%c", ch);
//     }

//     return;
// }

// 매개변수가 없는 함수는 매개변수 자리에 void를 사용한다.

// #include <stdio.h>

// int get_num(void);

// int main(void)
// {
//     int result;

//     result = get_num();
//     printf("반환값 : %d\n", result);
//     return 0;
// }

// int get_num(void) //괄호만 사용하는 것도 가능하지만 void를 넣어 매개변수가 없음을 명시적으로 표현하는 것이 좋다.
// {
//     int num;

//     printf("양수 입력 : ");
//     scanf("%d", &num);
//     while (num < 0)
//     {
//         printf("Please Input a positive number.\n")
//         printf("Input Positive number : ")
//         scanf("%d", &num);
//     }

//     return num;
// }