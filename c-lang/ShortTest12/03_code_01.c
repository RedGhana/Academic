#include <stdio.h>
#define A_MONEY 820
#define B_MONEY 960

int main(void) {
    FILE *fp;
    char file_name[64] = {'\0'};
    double a_time[100] = {0}, b_time[100] = {0};
    double sum_a = 0, sum_b = 0, sum_all = 0;
    int money = 0;
    int i, num = 0;
    
    printf("バイトのログを指定して下さい: ");
    scanf("%s", file_name);
    
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
    
    return 0;
}