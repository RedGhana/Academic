#include <stdio.h>

int main(void) {
    double num;
    printf("数値(小数)を入力してください:");
    scanf("%lf", &num);
    
    printf("変数「num」に代入された値は「%f」です。\n", num);
    
    // num上書き
    printf("数値(小数)を入力してください:");
    scanf("%lf", &num);
    printf("変数「num」は「%lf」に変更されました。\n", num);
    
    return 0;   
}