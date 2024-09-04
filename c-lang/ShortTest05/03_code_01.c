#include <stdio.h>

int main(void) {
    int score;
    printf("1週間にコーヒーを飲む量(杯)は?: ");
    scanf("%d", &score);
    if (score < 0) {
        printf("エラー\n");
        return 0;
    }
    
    if (score == 0) {
        printf("コーヒーは嫌いですか?\n");
    } else if (score <= 3) {
        printf("まずまずですね\n");
    } else if (score <= 7) {
        printf("かなりのコーヒー好きすね\n");
    } else if (score > 7) {
        printf("カフェイン中毒では?\n");
    }
    
    
    return 0;   
}