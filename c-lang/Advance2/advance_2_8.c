#include <stdio.h>

int main(void) {
    char a = 0x06;
    char b, c;
    char d = -1;
    char e, f;
    unsigned char g = -1;
    unsigned char h, i;
    
    printf("a = %x\n", a);
    b = a << 3;
    printf("%x << %x -> %x\n", a, 3, b);
    c = b >> 2;
    printf("%x >> %x -> %x\n\n", b, 2, c);
    
    // 算術シフト
    printf("d = %x\n", d);
    e = d >> 2;
    printf("%x >> %x -> %x\n", d, 2, e);
    f = e << 3;
    printf("%x << %x -> %x\n", e, 3, f);
    
    // 論理シフト
    printf("g = %x\n", g);
    h = g >> 2;
    printf("%x >> %x -> %x\n", g, 2, h);
    i = h << 3;
    printf("%x << %x -> %x\n", h, 3, i);
    
    return 0;   
}