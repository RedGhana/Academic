#include <stdio.h>
#define A_MONEY 820
#define B_MONEY 960

int main(void) {
    FILE *fp;
    char file_name[64] = {'\0'};
    char mode = 0;
    double a_time[100] = {0}, b_time[100] = {0};
    double sum_a = 0, sum_b = 0, sum_all = 0;
    double append_a = 0, append_b = 0;
    int money = 0;
    int i, num = 0;
    
    printf("*** バイト代管理アプリ\n");
    printf("バイトのログを指定して下さい: ");
    scanf("%s", file_name);
    
    getchar();
    printf("メニューを選択(バイト代の確認[c] / 時間の入力[a]): ");
    scanf("%c", &mode);
    
    if(mode == 'c') {
        fp = fopen(file_name, "r");
        if(fp == NULL) {
            printf("ファイルが開けませんでした\n");
            return 1;
        }
        
        while(fscanf(fp, "%lf %lf", &a_time[num], &b_time[num]) == 2) {
            num++;
        }
        for(i=0; i<num; i++) {
            sum_a += a_time[i];
            sum_b += b_time[i];
        }
        
        sum_all = sum_a + sum_b;
        money = (int)( (sum_a * A_MONEY) + (sum_b * B_MONEY) );
        printf("この月の労働時間のA枠が%.02f時間、B枠が%.02f時間, 合計は%.02f時間.\n", sum_a, sum_b, sum_all);
        printf("この月の給料は%d円の見込みです.\n", money);
        fclose(fp);
    } else if(mode == 'a') {
        fp = fopen(file_name, "a");
        if(fp == NULL) {
            printf("ファイルが開けませんでした\n");
            return 1;
        }
        
        printf("新たにA枠で何時間働きましたか?: ");
        scanf("%lf", &append_a);
        printf("新たにB枠で何時間働きましたか?: ");
        scanf("%lf", &append_b);
        
        fprintf(fp, "%.01f %.01f\n", append_a, append_b);
        printf("労働時間を追加しました\n");
        fclose(fp);
    } else {
        printf("正しいメニューを選択してください\n");
    }
    
    
    
    
    
    return 0;
}