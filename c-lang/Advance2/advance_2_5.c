#include <stdio.h>

int main(void) {
    int a = 0x00;
    
    printf("0x00の0bit目を1にすると、0x%02x", a | 0x01);
    
    return 0;   
}