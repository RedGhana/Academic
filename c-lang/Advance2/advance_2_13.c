#include <stdio.h>

int main(void) {
    unsigned int a = 0x1234, b = 0;
    
    b = a & 0x00ff;
    a = a>>8;
    printf("a = 0x%02x \n", a );
    printf("b = 0x%02x \n", b );
    
    return 0;   
}