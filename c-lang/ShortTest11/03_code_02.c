#include <stdio.h>

typedef struct Time{
    int hour;
    int minutes;
    int seconds;
} Time;

void increment_1sec(Time *t1);
void print_time(Time value);

int main(void) {
    Time input_time = {0};
    
    printf("*** 現在の時間を入力\n");
    
    printf("時：");
    scanf("%d", &input_time.hour);
    printf("分：");
    scanf("%d", &input_time.minutes);
    printf("秒：");
    scanf("%d", &input_time.seconds);
    
    increment_1sec(&input_time);
    printf("*** 1秒経過しました. 現在の時刻は...\n");
    print_time(input_time);
    
    return 0;
}

void increment_1sec(Time *t1) {
    t1->seconds ++;
    if(t1->seconds >= 60) {
        t1->seconds = 0;
        t1->minutes ++;

        if(t1->minutes >= 60) {
            t1->minutes = 0;
            t1->hour ++;
            if(t1->hour >= 24) {
                t1->hour = 0;
            }
        }
    }
}

void print_time(Time value) {
    printf("%02d時%02d分%02d秒\n", value.hour, value.minutes, value.seconds);
}