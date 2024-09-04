#include <stdio.h>

int main(void) {
    char a = 'X', b = 'Y', c = 'Z', tmp;
    printf("変数aの値は%c, 変数bの値は%c, 変数cの値は%cです\n", a, b, c);
    
    printf("変数aと変数bと変数cの値を交換します\n");
    
    tmp = c;
    c = b;
    b = a;
    a = tmp;
    
    printf("変数aの値は%c, 変数bの値は%c, 変数cの値は%cです\n", a, b, c);
    
    return 0;   
}