#include <stdio.h>

int main(void) {
    int day;
    printf("今日は何日ですか? ");
    scanf("%d", &day);
    if (day < 1 || day > 31) {
        printf("エラー\n");
        return 0;
    }
    
    switch (day % 7) {
        case 1:
            printf("月曜日ですね. お肉の特売日です.\n");
            break;
        case 2:
            printf("火曜日ですね. 魚の特売日です.\n");
            break;
        case 3:
            printf("水曜日ですね. お米の特売日です.\n");
            break;
        case 4:
            printf("木曜日ですね. 野菜の特売日です.\n");
            break;
        case 5:
            printf("金曜日ですね. お酒の特売日です.\n");
            break;
        case 6:
            printf("土曜日ですね. お菓子の特売日です.\n");
            break;
        case 0:
            printf("日曜日ですね. お菓子の特売日です.\n");
            break;
        default :
            printf("エラー\n");
            break;
    }
    
    return 0;
}