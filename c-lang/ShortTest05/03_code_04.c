#include <stdio.h>

int main(void) {
    char moji;
    
    printf("何か好きな1文字を入力してください: ");
    scanf("%c", &moji);
    
    if (moji >= 0x30 && moji <= 0x39) {
        printf("あなたの入力した文字は, 数字です.\n");
    } else {
        printf("あなたの入力した文字は, 数字ではない文字です.\n");
    }
    
    return 0;
}