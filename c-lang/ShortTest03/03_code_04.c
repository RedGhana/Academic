#include <stdio.h>

int main(void) {
    // 初期値
    int a = 50, b = 100, c = 150, d = 200, tmp;
    printf("変数aの値は%d,変数bの値は%d,変数cの値は%d,変数dの値は%dです\n", a, b, c, d);
    
    // 入れ替え処理
    printf("変数aと変数bと変数cと変数dの値を交換します\n");
    tmp = d;
    d = a;
    
    a = b;
    
    b = c;

    c = tmp;
    
    
    // 結果表示
    printf("変数aの値は%d,変数bの値は%d,変数cの値は%d,変数dの値は%dです\n", a, b, c, d);
    return 0;   
}