#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    int *pi;
    int i, sum = 0;

    pi = (int *)malloc(5 * sizeof(int));
    if (pi ==NULL)
    {
        printf("#�޸𸮰� �����մϴ�.\n");
        exit(1);
    }

    printf("5���� ���̸� �Է��ϼ���. : ");
    for (i = 0; i < 5; i++)
    {
        scanf("%d", &pi[i]);
        sum += pi[i];
    }
    printf("5���� ��� ���� : %.1lf\n", (sum / 5.0));
    free(pi);

    return 0;
}