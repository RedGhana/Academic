#include <stdio.h>

int main(void) {
    int a = 0xAA;
    
    printf("0xaaの0,1,2,3bit目を1にすると、0x%02x", a | 0x0f);
    
    return 0;   
}