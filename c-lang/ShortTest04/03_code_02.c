#include <stdio.h>

int main(void) {
    int tax_w, price;
    double tax;
    printf("現在の税率(%%)を入力してください:");
    scanf("%d", &tax_w);
    tax_w = 100 + tax_w;
    tax = tax_w * 0.01;
    
    price = (int)(600 * tax);
    printf("1パック50個入りのLEDは,税込み%d円です.\n", price);
    
    printf("LED1つあたりの単価は%.1f円となります.\n", (double)price / 50.0);
    
    return 0;   
}