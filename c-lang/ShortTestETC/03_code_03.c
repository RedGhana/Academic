#include <stdio.h>

typedef enum Color {
    RED, BLUE, GREEN, BLANK
} Color;

void output_led(Color c);

int main(void) {
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