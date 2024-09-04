#include <stdio.h>

int main(void) {
    int h, w, tmp_h, tmp_w;
    printf("横の長さ: ");
    scanf("%d", &w);
    if(w < 1) {
        printf("エラー\n");
        return 0;
    }
    printf("縦の長さ: ");
    scanf("%d", &h);
    if(h < 1) {
        printf("エラー\n");
        return 0;
    }
    
    for(tmp_h = h; tmp_h > 0; tmp_h--) {
        for(tmp_w = w; tmp_w > 0; tmp_w--) {
            printf("*");
        }
        printf("\n");
    }
    
    return 0;   
}