#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    char str[100], str2[100];
    int mode=0, len;
    printf("好きな文字列を入力してください：");
    scanf("%s", str);
    
    printf("動作モードを選択してください (0：文字数カウント　1：文字列コピー　2：文字列結合　3：文字数比較　4：文字列→数値変換)：");
    scanf("%d", &mode);
    
    printf("\n");
    switch(mode) {
        case 0:
            printf("文字列「%s」は%d文字\n", str, strlen(str));
            break;
        case 1:
            strcpy(str2, str);
            printf("文字列「%s」をstr2にコピーしました\n", str);
            printf("str1: %s\n", str);
            printf("str2: %s\n", str2);
            break;
        case 2:
            printf("結合したい文字列を入力してください：");
            scanf("%s", str2);
            // strcatは文字数に制限がないが、strncatでは連結する文字数に制限を設けることができる
            strncat(str, str2, 50);
            printf("結合した結果は「%s」になりました\n", str);
            break;
        case 3:
            printf("比較したい文字列を入力してください：");
            scanf("%s", str2);
            if(strcmp(str, str2) == 0) {
                printf("strとstr2は一致しています\n");
            } else {
                printf("strとstr2は不一致です\n");
            }
            break;
        case 4:
        // 文字列「123」を数値「123」に変換
            printf("文字列「%s」を数値に変換すると%dです\n", str, atoi(str));
            break;
        default:
            printf("正しい動作モードを選択してください\n");
            break;
    }
    
    return 0;
}