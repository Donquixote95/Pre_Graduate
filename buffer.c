//stdin, stdout
//Charater I/O function ; fgetc, fputc
//parameter가 필요하다. 이외 기능은 getchar, putchar와 같다.
//fgetc는 stdin(standard input ; 키보드와 연결된 버퍼의 이름)을 주고 fputc는 stdout(출력 버퍼)을 준다.

#include <stdio.h>
int main(void)
{
    int ch;
    int cnt = 0;
    ch = getchar();

    while(ch != '\n')
    {
        if ((ch>=97) && (ch <= 122)) // or (ch >= 'a') && (ch <= 'z')
        {
            cnt++;
        }
        ch = getchar();
    }
    printf("The number of small charaters : %d\n", cnt);

    return 0;
}

//입력 버퍼 지우기
//scanf, getchar 함수는 같은 버퍼를 사용하며 입력 데이터를 공유한다.
//앞서 실행한 입력 함수가 버퍼에 남겨둔 데이터를 그 이후에 함수가 잘못 사용할 수 있다.
//버퍼에 남아 있는 문자들을 모두 입력해서 사용하지 않고 버리면 된다.
// #include <stdio.h>

// int main(void)
// {
//     int num, grade;

//     printf("Student number : ");
//     scanf("%d", &num);
//     getchar(); // buffer에 남은 개행문자(\n) 제거
//     printf("Grade : ");
//     grade = getchar();
//     printf("Student number : %d, Grade : %c", num, grade);

//     return 0;
// }

//getchar 함수를 사용한 문자열 출력
// #include <stdio.h>

// void my_gets(char *str, int size);

// int main(void)
// {
//     char str[7];

//     my_gets(str, sizeof(str));
//     printf("Input : %s\n", str);

//     return 0;
// }

// void my_gets(char *str, int size)
// {
//     int ch;
//     int i = 0;

//     ch = getchar();
//     while ((ch != '\n') && (i < size - 1))
//     {   
//         str[i] = ch;
//         i++;
//         ch = getchar();
//     }
//     str[i] = '\0'; //입력된 문자열의 끝에 널 문자 저장
// }


// 버퍼 ; 프로그램에서 직접 할당하는 것이 아니라 프로그램을 실행하는 중에 운영체제가 자동으로 할당하는 메모리의 저장 공간
// 키보드로 입력하는 데이터는 일단 버퍼에 저장된 후에 scanf 함수에 의해 변수에 입력된다.
// 버퍼는 데이터를 보관하는 역할을 한다. 최초 입력할 떄 필요한 데이터를 한꺼번에 저장해놓으면 scanf 함수는 호출 즉시 버퍼에서 데이터를 가져올 수 있다.
// 입력 데이터는 Enter 를 누르는 순간 버퍼에 저장되며 개행 문자도 함께 저장된다.

// #include <stdio.h>

// int main(void)
// {
//     int res;
//     char ch;

//     while(1)
//     {
//         res = scanf("%c", &ch);
//         if (res == EOF) break; // End Of File ; -1 대신에 입력의 끝을 의미하는 이름
        // stdio.h 헤더 파일에는 소스 코드에 있는 EOF 라는 이름을 -1로 바꾸는 전처리 지시자가 있다.
        // if (res == -1) break;
    //     printf("%d", ch);
    // }

    // char ch;
    // int i;

    // for(i = 0; i <3; i++)
    // {
    //     scanf("%c", &ch);
    //     printf("%c", ch);
    // }

    // while (1)
    // {
    //     scanf("%c", &ch);
    //     if (ch == '\n') 
    //     {
    //         break;
    //     }
    //     printf("%c", ch);
    // }

//     return 0;
// }

//scanf 함수 반환값 활용
// 이유 ; 개행 문자 또한 하나의 입력 데이터로 쓴다면 입력을 종료하는 별도의 신호가 필요하다.
// scanf 함수는 키보드로 Ctrl + Z를 누르면 -1을 반환한다. 
// 운영체제에 따라서는 Ctrl + Z를 누르고 Enter를 누른 후에 Ctrl + Z를 한 번 더 입력해야 -1을 반환한다.
// 유닉스나 리눅스 시스템에서는 Ctrl + D를 사용한다.
// 결국 scanf 함수가 -1을 반환하기 전까지 개행 문자를 포함한 모든 문자를 데이터로 사용할 수 있다.

