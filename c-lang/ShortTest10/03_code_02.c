#include <stdio.h>
int count_target_char(char *str, char target);

int main(void) {
    char str[100], target;
    int result=0;
    printf("好きな文字列を入力：");
    scanf("%s", str);
    printf("数えたい文字は？：");
    getchar();
    scanf("%c", &target);
    
    result = count_target_char(str, target);
    
    printf("文字%cは%d文字含まれています.", target, result);
    
    return 0;
}

int count_target_char(char *str, char target) {
    int i, result=0;
    for(i=0; *(str+i) != '\0'; i++) {
        if(*(str+i) == target) {
            result ++;
        }
    }
    return result;
}