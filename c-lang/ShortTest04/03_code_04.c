#include <stdio.h>

int main(void) {
    char ch;
    int num;
    printf("数字(0~9)を1文字入力:");
    ch = getchar();
    printf("あなたが入力した数字は%c, 16進数では0x%xです.\n", ch , ch);
    
    num = (int)ch - 0x30;
    printf("変数「ch」の値を整数値に変換しました.\n");
    printf("変換した整数値に, 10を加算した結果は %d です.\n", num += 10);
    
    return 0;   
}