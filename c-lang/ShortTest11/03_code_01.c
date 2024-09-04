#include <stdio.h>

typedef struct Time{
    int hour;
    int minutes;
    int seconds;
} Time;

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
    
    printf("*** 入力された時間は以下の通り\n");
    print_time(input_time);
    
    return 0;
}

void print_time(Time value) {
    printf("%02d時%02d分%02d秒\n", value.hour, value.minutes, value.seconds);
}