#include <stdio.h>

int main(void) {
    double teimenseki;
    double taiseki;
    int a = 3, b = 5, c = 5;
    
    teimenseki = a * b / 2.0;
    taiseki = teimenseki * c / 3.0;
    
    printf("底面の面積: %.2f cm2\n", teimenseki);
    printf("三角形の体積: %.2f cm3\n", taiseki);
    
    return 0;   
}