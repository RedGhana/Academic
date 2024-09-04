#include <stdio.h>

#define KAMOKU 4

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

int check_denken(Denken result);

int main(void) {
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