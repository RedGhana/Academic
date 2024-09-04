#include <stdio.h>

typedef struct Time{
    int hour;
    int minutes;
    int seconds;
} Time;

typedef struct DayTime{
    int day;
    Time time;
} DayTime;

void increment_1sec(DayTime *dt1);
void print_time(DayTime value);

int main(void) {
    DayTime dt = {0};
    
    printf("*** 日数と時間を入力\n");
    
    printf("日：");
    scanf("%d", &dt.day);
    printf("時：");
    scanf("%d", &dt.time.hour);
    printf("分：");
    scanf("%d", &dt.time.minutes);
    printf("秒：");
    scanf("%d", &dt.time.seconds);
    
    increment_1sec(&dt);
    printf("*** 1秒経過\n");
    print_time(dt);
    
    return 0;
}

void increment_1sec(DayTime *dt1) {
    dt1->time.seconds ++;
    if(dt1->time.seconds >= 60) {
        dt1->time.seconds = 0;
        dt1->time.minutes ++;

        if(dt1->time.minutes >= 60) {
            dt1->time.minutes = 0;
            dt1->time.hour ++;
            if(dt1->time.hour >= 24) {
                dt1->time.hour = 0;
                dt1->day ++;
            }
        }
    }
}

void print_time(DayTime value) {
    printf("%02d日と%02d時%02d分%02d秒\n", value.day, value.time.hour, value.time.minutes, value.time.seconds);
}