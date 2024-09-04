#include <stdio.h>

int main(void) {
    FILE *fp;
    char file_name[64] = {'\0'};
    char ch = '\0';
    int sum_word = 0;
    int i, num = 0;
    
    printf("開くファイルは?: ");
    scanf("%s", file_name);
    
    fp = fopen(file_name, "r");
    if(fp == NULL) {
        printf("ファイルが開けませんでした\n");
        return 1;
    }
    
    while( (ch = fgetc(fp)) != EOF) {
        // 半角スペース or 改行で1単語
        if(ch == ' ' || ch == '\n') {
            sum_word++;
        }
    }
    // EOFで1単語
    sum_word++;
    
    printf("本ファイルに含まれる単語の数は%d語です.\n", sum_word);
    
    fclose(fp);
    
    return 0;
}