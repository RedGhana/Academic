#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM 10000

void bubble_sort(int *list, int len);
int compare(const void *a, const void *b);

int main(void) {
    // 変数宣言
    int array[] = {
        #include "data.txt"
    };
    int i;
    char ch;
    
    printf("どちらのソート?(b / q): ");
    ch = getchar();
    
    
    // 処理開始前の時間を取得
    int t = clock();
    
    // 昇順にソート
    if(ch == 'b') {
        bubble_sort(array, NUM);
    } else {
        qsort(array, NUM, sizeof(int), compare);
    }
    
    // 処理開始後の時間とクロックを取得
    printf("%.6f秒\n", (double)(clock()-t)/CLOCKS_PER_SEC);
    
    return 0;
}

void bubble_sort(int *list, int len) {
    int i, j, tmp;
    for(i=0; i<len-1; i++) {
        for(j=i+1; j<len; j++) {
            if(list[i] > list[j]) {
                tmp = list[i];
                list[i] = list[j];
                list[j] = tmp;
            }
        }
    }
}

int compare(const void *a, const void *b) {
    const int *pi1 = a;
    const int *pi2 = b;
    
    if(*pi1 < *pi2) {
        return -1;
    } else if(*pi1 > *pi2) {
        return 1;
    } else {
        return 0;
    }
}
