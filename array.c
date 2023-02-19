#include <stdio.h>
#include <string.h> //문자열과 관련된 함수 원형을 모아놓은 헤더 파일

int main(void)
{
    //문자열 전용 IO함수 : gets, puts

    char str[80]; 
    printf("Input chaters : ");
    gets(str);
    puts("Output chaters : ");
    puts(str);

    return 0;

    //초기화한 문자들은 배열의 처음부터 차례로 저장되어 문자열을 만든다. 남는 배열 요소에는 자동으로 0이 채워진다.
    //모든 문자는 아스키 코드 값으로 저장되므로 결국 널 문자는 아스키 코드 값이 0인 문자를 말한다.
    //문자 상수로는\0으로 표현된다.
    //null character ; char형 배열에 저장된 0, 문자열의 끝을 표시화는 용도로 쓰인다.
    
    //char형 배열을 선언해서 문자열을 저장하려면 문자열보다 하나 더 크게 선언해야 한다. 왜냐하면 null character(\0)를 저장해야 하기 때문이다.

    //char형 배열 선언 시 초기화를 하면 남는 배열 요소가 0으로 채워지므로 자동으로 문자열의 끝에 널 문자가 저장되나, 초기화하지 않은 상태에서
    //배열요소에 문자를 직접 대입한다면 반드시 마지막 문자 다음에는 널 문자를 대입해야 한다.
    // char str[80];
    // str[0] = 'a';
    // str[1] = 'p';
    // str[2] = 'p';
    // str[3] = 'l';
    // str[4] = 'e';
    // str[5] = '\0';

    //char형 배열 선언 시 주의할 점 ; 대입 연산자는 사용 불가능하다. 문자열의 길이가 다를 수 있기 때문에
    //strcpy 함수를 사용한다.

    // char str1[80] = "cat";
    // char str2[80];

    // strcpy(str1, "tiger");
    // strcpy(str2, str1);
    // printf("%s, %s\n", str1, str2);

    // return 0;

    // char str[80] = "applejam";

    // printf("최초 문자열 : %s\n", str);
    // printf("문자열 입력 : ");
    // scanf("%s", str);
    // printf("입력 후 문자열 : %s\n", str);

    // return 0;
    
    //sizeof 연산자를 활용한 배열 처리
    // int score[5];
    // int i;
    // int total = 0;
    // double avg;
    // int count;

    // count = sizeof(score) / sizeof(score[0]); // 배열 요소의 개수를 계산


    // for (i=0; i<count; i++)
    // {
    //     scanf("%d", &score[i]);
    // }

    // for (i=0; i<count; i++)
    // {
    //     total += score[i];
    // }
    // avg = total / (double)count;

    // for(i=0; i<count; i++)
    // {
    //     printf("%5d", score[i]);
    // }
    // printf("\n");

    // printf("average : %.1lf\n", avg);

    // return 0;

    // int aray1[5] = {1,2,3,4,5};
    // int aray2[5] = {1,2,3}; //왼쪽부터 차례로 1, 2, 3으로 초기화하고 남은 element는 0으로 채운다.
    // int ary3[] = {1,2,3}; // 컴파일러는 초깃값 개수만큼 배열 요소 개수를 정하고 저장 공간을 할당한다.

    // double ary4[5] = {1.0, 2.1, 3.2, 4.3, 5.4};
    // char ary5[6] = {'a', 'p', 'p', 'l', 'e'};

    // int ary[5];

    // ary[0] = 10;
    // ary[1] = 20;
    // ary[2] = ary[0] + ary[1];
    // scanf("%d", &ary[3]);

    // printf("%d\n", ary[2]);
    // printf("%d\n", ary[3]);
    // printf("%d\n", ary[4]);

    // return 0;
}