#include <stdio.h>

int main(void) {
    char ch;
    printf("1文字入力してください:");
    ch = getchar();
    
    printf("入力された文字を整数で表すと,10進数では%dです.16進数は0x%xです。\n", ch, ch);
    
    return 0;   
}