// 関数形式マクロ、列挙体、共用体、ビットフィールド、構造体との組み合わせ
#include <stdio.h>
#include "03_header.h"

#define KAMOKU 4

#define calc_c(v, r) (v / r)
#define ascii_code(ch) (printf("%c(0x%02X)", ch, ch))

typedef enum Color {
    RED, BLUE, GREEN, BLANK
} Color;

typedef struct Exam {
    unsigned int theory;
    unsigned int power;
    unsigned int machine;
    unsigned int regulations;
} Exam;

typedef union Denken {
    Exam exam;
    unsigned int score[4];
} Denken;

typedef struct BitTest {
    unsigned int tmp:2;
} Bit;

int GlobalNum;

// プロトタイプ宣言
int check_denken(Denken result);

void output_led(Color c);


int calc_current() {
    double v;
    int r;
    printf("電圧値[V]は？:");
    scanf("%lf", &v);
    printf("抵抗値[Ω]は？:");
    scanf("%d", &r);
    printf("電流値は%.4f[A]です\n", calc_c(v,r));
    
    return 0;
}

int show_ascii_code() {
    char ch;
    printf("確認したい文字:");
    getchar();
    ch = getchar();
    printf("ASCIIコードは");
    ascii_code(ch);
    printf("です\n");
    
    return 0;
}

int temp_led() {
    Color color = BLANK;
    int temp = 0;
    
    printf("今、何℃？:");
    scanf("%d", &temp);
    
    if(temp < 5) {
        color = BLUE;
    } else if(temp < 20) {
        color = BLANK;
    } else if(temp < 30) {
        color = GREEN;
    } else {
        color = RED;
    }
    
    output_led(color);
    
    return 0;
}

void output_led(Color c) {
    switch(c) {
        case RED:
            printf("LEDが赤に点灯\n");
            break;
        case BLUE:
            printf("LEDが青に点灯\n");
            break;
        case GREEN:
            printf("LEDが緑に点灯\n");
            break;
        case BLANK:
            printf("LEDが消灯\n");
            break;
        default :
            printf("不明な色です\n");
            break;
    }
}

int score_check() {
    Denken score;
    int result = 0;
    
    printf("理論の点数は？:");
    scanf("%d", &score.exam.theory);
    printf("電力の点数は？:");
    scanf("%d", &score.exam.power);
    printf("機械の点数は？:");
    scanf("%d", &score.exam.machine);
    printf("法規の点数は？:");
    scanf("%d", &score.exam.regulations);
    
    result = check_denken(score);
    if(result == 1) {
        printf("あなたは合格です\n");
    } else {
        printf("あなたは不合格です\n");
    }
    
    return 0;
}

int check_denken(Denken result) {
    int check, i;
    for(i=0; i<KAMOKU; i++) {
        if(result.score[i] < 60) {
            check = 0;
            break;
        } else {
            check = 1;
        }
    }
    
    return check;
}

void add_global() {
    printf("GlobalNumに設定する数値: ");
    scanf("%d", &GlobalNum);
}