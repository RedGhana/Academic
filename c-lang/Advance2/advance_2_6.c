#include <stdio.h>

int main(void) {
    int a = 0x00;
    
    printf("0x00の0,1,4,7bit目を1にすると、0x%02x", a | 0x93);
    
    return 0;   
}