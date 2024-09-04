#include <stdio.h>

#define calc_current(v, r) (v / r)

int main(void) {
    double v;
    int r;
    printf("電圧値[V]は？:");
    scanf("%lf", &v);
    printf("抵抗値[Ω]は？:");
    scanf("%d", &r);
    printf("電流値は%.4f[A]です\n", calc_current(v,r));
    
    return 0;
}