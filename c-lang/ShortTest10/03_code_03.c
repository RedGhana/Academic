#include <stdio.h>
void sort_asc(int *array, int length);
int upper_swap(int *upper, int *lower);
void print_array(int *array, int length);

int main(void) {
    int length=5, i;
    int a[5]={30,10,40,20,50};
    char input_order;
    
    printf("初期の配列aは以下の通り\n配列の中身は, ");
    for(i=0; i<length; i++) {
        printf("%d, ", a[i]);
    }
    printf("\n");
    
    
    sort_asc(a, length);
    
    print_array(a, length);
    
    
    return 0;
}

void sort_asc(int *array, int length) {
    int i, j;
    for(i=0; i<length-1; i++) {
        for(j=i+1; j<length; j++) {
            upper_swap( (array+i), (array+j) );
        }
    }
    
}

int upper_swap(int *upper, int *lower) {
    int tmp, result=0;
    if( *upper > *lower ) {
        tmp = *upper;
        *upper = *lower;
        *lower = tmp;
        result = 1;
    }
    return result;
}

void print_array(int *array, int length) {
    int i;
    printf("並べ替えた後の配列aは以下の通り\n配列の中身は,  ");
    for(i=0; i<length; i++) {
        printf("%d, ", array[i]);
    }
}