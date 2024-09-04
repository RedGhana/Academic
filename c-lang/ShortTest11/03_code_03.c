#include <stdio.h>

typedef struct Time{
    int hour;
    int minutes;
    int seconds;
} Time;

Time diff_time(Time t1, Time t2);
void print_time(Time value);

int main(void) {
    Time time1 = {0}, time2 = {0}, result_time = {0};
    
    printf("*** 昨晩の就寝時間は? (24時間表記)\n");
    
    printf("時：");
    scanf("%d", &time1.hour);
    printf("分：");
    scanf("%d", &time1.minutes);
    printf("秒：");
    scanf("%d", &time1.seconds);
    
    printf("*** 今朝の起床時間は? (24時間表記)\n");
    
    printf("時：");
    scanf("%d", &time2.hour);
    printf("分：");
    scanf("%d", &time2.minutes);
    printf("秒：");
    scanf("%d", &time2.seconds);
    
    result_time = diff_time(time1, time2);
    printf("*** 1秒経過しました. 現在の時刻は...\n");
    print_time(input_time);
    
    return 0;
}

Time diff_time(Time t1, Time t2) {
    int t1_con=0, t2_con=0;
    
    t1_con = t1.seconds;
    t1_con += t1.minutes * 60;
    t1_con += t1.hour * 3600;
    
    
    t2_con = t2.seconds;
    t2_con += t2.minutes * 60;
    t2_con += t2.hour * 3600;
    
    t1_con = t1_con - t2_con;
    
    if(t1_con >=
}

void print_time(Time value) {
    printf("%02d時%02d分%02d秒\n", value.hour, value.minutes, value.seconds);
}