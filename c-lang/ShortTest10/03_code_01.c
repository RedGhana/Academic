#include <stdio.h>
void print_array_details(int *array, int len);

int main(void) {
    int nums[] = { 2,4,6,8,10,12,14,16 };
    int len=8;
    print_array_details(nums, len);
    return 0;
}

void print_array_details(int *array, int len) {
    int i;
    printf("配列の先頭アドレス：%p\n", array);
    printf("配列の末尾アドレス：%p\n", array+len-1);
    printf("配列の中身は");
    for(i=0; i<len; i++) {
        printf(", %d", *(array+i) );
    }
    printf("\n");
}