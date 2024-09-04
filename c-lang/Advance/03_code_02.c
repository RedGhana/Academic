#include <stdio.h>

int main(void) {
    double temp;
    printf("室温を入力: ");
    scanf("%lf", &temp);
    
    if(temp < 23.0) {
        printf("寒いです\n");
    } else if(temp < 27.0) {
        printf("適温です\n");
    } else{
        printf("暑いです\n");
    }
    
    return 0;   
}