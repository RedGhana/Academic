#include <stdio.h>

int main(void) {
    int a = 0xff;
    
    printf("0xffの2bit目と4bit目の値を0にすると、0x%02x", a ^ 0x14);
    
    return 0;   
}