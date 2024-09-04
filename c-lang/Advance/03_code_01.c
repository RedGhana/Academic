#include <stdio.h>

int main(void) {
    int age;
    printf("年齢を入力: ");
    scanf("%d", &age);
    
    if( age == 25 ) {
        printf("厄年です\n");
    } else if( age == 42 ) {
        printf("厄年です\n");
    } else if( age == 61 ) {
        printf("厄年です\n");
    } else {
        printf("厄年ではないです\n");
    }
    
    return 0;   
}