#include <stdio.h>

int main(void) {
    int num = 300;
    printf("変数「num」に代入された値は「%d」です。\n", num);
    
    // num上書き
    num = 10;
    printf("変数「num」は「%d」に変更されました。\n", num);
    
    
    // num上書き2
    num = 100;
    printf("変数「num」は「%d」に変更されました。\n", num);
    
    return 0;   
}