#include <stdio.h>

int main(void) {
    unsigned int a = 0xAB, b = 0xCD;
    
    printf("(a<<8) | b = 0x%04x \n", (a<<8) | b );
    
    return 0;   
}