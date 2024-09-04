#include <stdio.h>

int main(void) {
    char ch = 'M';
    
    printf("変数「ch」には%cが代入されています。整数で表すと...\n10進数では%dです。16進数では0x%xです。", ch, ch , ch);
    
    return 0;   
}