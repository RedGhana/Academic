#include <stdio.h>

int main(void) {
    int num = 123;
    printf("変数「num」に代入された値は「%d」です。\n", num);
    
    num -= 23;
    printf("演算の結果, 変数「num」は「%d」に変更されました。\n", num);
    
    num *= 10;
    printf("演算の結果, 変数「num」は「%d」に変更されました。\n", num);
    
    
    return 0;   
}