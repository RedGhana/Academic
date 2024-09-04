#include <stdio.h>
#define NUM_LEN 5

void sort_array(int *source, int length, int order);
void print_array(int *array, int length);
double calc_avg_array(int *array, int length);
int seek_min_array(int *array, int length);
int count_upper_array(int *array, int length, int threshold);

int main(void) {
    int length=NUM_LEN, order, i, mode = 0, min = 0, count = 0, threshold=0;
    int num[NUM_LEN] = {0};
    double avg = 0;
    char input_order;
    
    printf("配列numに格納する値を%dつ入力してください\n", NUM_LEN);
    for(i=0; i<NUM_LEN; i++) {
        scanf("%d", &num[i]);
    }
    printf("配列numに格納された値を表示します\n");
    print_array(num, length);
    
    printf("\n");
    printf("動作モードを選択してください (0：並び替え　1：平均値算出　2：最小検索　3：条件検索：");
    scanf("%d", &mode);
    
    printf("\n");
    switch(mode) {
        case 0:
            getchar();
            printf("\n並び替えの順は?（昇順：a，降順：d）：");
            scanf("%c", &input_order);
            switch(input_order) {
                case 'a': 
                    order = 0;
                    printf("\n\n配列numを昇順に並べ替えました\n");
                    break;
                case 'd': 
                    order = 1;
                    printf("\n\n配列numを降順に並べ替えました\n");
                    break;
                default:
                    order = 0;
                    printf("\n\n配列numを昇順に並べ替えました\n");
                    break;
            }
            
            sort_array(num, length, order);
            
            
            printf("配列num: ");
            print_array(num, length);
            break;
        case 1:
            avg = calc_avg_array(num, length);
            printf("配列numに格納された値の平均は%.2fです\n", avg);
            break;
        case 2:
            min = seek_min_array(num, length);
            printf("配列numの中で最も小さい値は%dです\n", min);
            break;
        case 3:
            printf("いくつ以上を探索しますか: ");
            scanf("%d", &threshold);
            count = count_upper_array(num, length, threshold);
            printf("配列numの中で検索条件に合致した件数は%dです\n", count);
            break;
        default :
            printf("正しい動作モードを選択してください\n");
            break;
    }
    
    
    return 0;
}

void sort_array(int *source, int length, int order) {
    int i, j, tmp;
    switch(order) {
        case 0:
            for(i=0; i<length-1; i++) {
                for(j=i+1; j<length; j++) {
                    if( *(source+i) > *(source+j) ) {
                        tmp = *(source+i);
                        *(source+i) = *(source+j);
                        *(source+j) = tmp;
                    }
                }
            }
            break;
        case 1:
            for(i=0; i<length-1; i++) {
                for(j=i+1; j<length; j++) {
                    if( *(source+i) < *(source+j) ) {
                        tmp = *(source+i);
                        *(source+i) = *(source+j);
                        *(source+j) = tmp;
                    }
                }
            }
            break;
    }
    
}

void print_array(int *array, int length) {
    int i;
    for(i=0; i<length; i++) {
        printf("%d, ", *(array+i) );
    }
}

double calc_avg_array(int *array, int length) {
    int i, _sum=0;
    for(i=0; i<length; i++) {
        _sum += *(array+i);
    }
    return _sum / (double)length;
}

int seek_min_array(int *array, int length) {
    int i, _min=*array;
    for(i=0; i<length-1; i++) {
        if( *(array+i) > *(array+i+1) )
        _min = *(array+i+1);
    }
    return _min;
}

int count_upper_array(int *array, int length, int threshold) {
    int i, counter=0;
    for(i=0; i<length; i++) {
        if( *(array+i) >= threshold ) {
            counter++;
        }
    }
    return counter;
}