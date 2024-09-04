#include <stdio.h>

int main(void) {
    int counter;
    
    printf("整数を入力: ");
    scanf("%d", &counter);
    
    while(counter > 0) {
        printf("%d\n", counter);
        counter --;
    }
    printf("終わり！\n");
    
    
    return 0;   
}