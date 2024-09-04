#include <stdio.h>

int main(void) {
    double value;
    
    printf("何か好きな1文字を入力してください: ");
    scanf("%lf", &value);
    
    if( value < 10) {
        printf("あなたの入力した文字は, 数字です.\n");
    } else {
        printf("あなたの入力した文字は, 数字ではない文字です.\n");
    }
    
    return 0;
}