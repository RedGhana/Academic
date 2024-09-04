#include <stdio.h>

#define show_ascii_code(ch) (printf("%c(0x%02X)", ch, ch))

int main(void) {
    char ch;
    printf("確認したい文字:");
    ch = getchar();
    printf("ASCIIコードは");
    show_ascii_code(ch);
    printf("です\n");
    
    return 0;
}