#include <stdio.h>

int main(void) {
    int A, B, C, score;
    
    printf("科目Aの点数: ");
    scanf("%d", &A);
    if (A < 0 || A > 100) {
        printf("エラー\n");
        return 0;
    }
    
    printf("科目Bの点数: ");
    scanf("%d", &B);
    if (B < 0 || B > 100) {
        printf("エラー\n");
        return 0;
    }
    
    printf("科目Cの点数: ");
    scanf("%d", &C);
    if (C < 0 || C > 100) {
        printf("エラー\n");
        return 0;
    }
    
    // 点数処理
    score = A + B + C;
    printf("3科目合計の点数は %d 点です.\n", score);
    if(A < 60 || B < 60 || C < 60 || score < 200) {
        printf("不合格です.\n");
    } else {
        printf("合格です.\n");
    }
    
    return 0;   
}