#include <stdio.h>

int main(void) {
    int tmp_score = 0, count = 1, sum_score;
    while(0 <= tmp_score && tmp_score <= 100) {
        printf("%d人目の点数は: ", count);
        scanf("%d", &tmp_score);
        if(0 <= tmp_score && tmp_score <= 100) {
            count++;
            sum_score += tmp_score;
        } else {
            count--;
            break;
        }
    }
    printf("%d人のテストの平均点は,%.2f点です.", count, (double)sum_score/count);
    
    return 0;   
}