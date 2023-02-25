// 배열에 값을 입력하는 함수

#include <stdio.h>

void input_ary(double *pa, int size);
double find_max(double *pa, int size);

int main(void)
{
    double ary[5];
    double max;
    int size = sizeof(ary) / sizeof(ary[0]);

    input_ary(ary, size);
    max = find_max(ary, size);
    printf("max value : %.1lf\n", max);

    return 0;
}

void input_ary(double *pa, int size)
{
    int i;

    printf("%d개의 실수값 입력 : ", size);
    for (i = 0; i < size; i++)
    {
        scanf("%lf", pa + i); //&pa[i]로 입력해도 된다.
    }
}

double find_max(double *pa, int size)
{
    double max;
    int i;

    max = pa[0]; // 첫 번쨰 요소의 값을 최댓값으로 지정
    for (i = 1; i < size; i++)
    {
        if (pa[i] > max)
        {
            max = pa[i];
        }
    }

    return max;
}