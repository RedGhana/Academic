#include <stdio.h>
#include <string.h>

int main(void) {
    char user[100]={0}, user_check[50]={0};
    int checker;
    printf("*** メールアドレス作成プログラム ***\n");
    printf("ユーザ名入力：");
    scanf("%s", user);
    
    printf("ユーザ名入力(確認)：");
    scanf("%s", user_check);
    
    checker = strcmp(user, user_check);
    switch(checker) {
        case 0:
            if( strlen(user) >= 32 || strlen(user) < 5) {
                printf("文字数は5文字以上、32文字未満にして下さい\n");
            } else {
                printf("メールアドレスを発行しました！\n");
                printf("%s", strcat(user, "@shikoku.com"));
            }
            break;
        default :
            printf("入力が不一致です\n");
            break;
    }
    
    return 0;
}
