#include <stdio.h>

int main(void) {
    int num;
    printf("数値(整数)を入力してください : ");
    scanf("%d", &num);
    
    printf("変数numに代入された値は「%d」です。\n", num);
    
    printf("数値(整数)を入力してください : ");
    scanf("%d", &num);
    printf("変数numは「%d」に変更されました。\n", num);
    
    printf("数値(整数)を入力してください : ");
    scanf("%d", &num);
    printf("変数numは「%d」に変更されました。\n", num);
    
    
    return 0;   
}