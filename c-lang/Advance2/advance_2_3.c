#include <stdio.h>

int main(void) {
    int a = 0xcc;
    
    printf("0xccから3bit目と7bit目の値だけ抽出すると、0x%02x", a & 0x88);
    
    return 0;   
}