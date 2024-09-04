#include <stdio.h>

int main(void) {
    unsigned int a = 0x8ff0;
    
    printf("0x8ff0 >> 4 = 0x%04x", (a >> 4) & 0xff );
    
    return 0;   
}