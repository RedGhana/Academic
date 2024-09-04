#include <stdio.h>

int main(void) {
    int a = 0xff;
    
    printf("0xffから下位4bitの値だけ抽出すると、0x%02x", a & 0x0f);
    
    return 0;   
}