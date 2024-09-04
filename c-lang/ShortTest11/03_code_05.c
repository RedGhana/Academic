#include <stdio.h>
#define STR_LEN 64
#define LIST_LEN 6

typedef struct Mouse {
    char name[STR_LEN];
    int price;
    double length;
    double weight;
    int button_num;
} Mouse;

void print_mouse_list(Mouse *list, int length);

int main(void) {
    Mouse mouse_list[LIST_LEN] = { {"MM190", 1182, 115.4, 89.9, 3}, {"MM221", 1399, 99, 77.1, 3}, {"MM235R", 1760, 95, 84, 3}, {"MM187", 1127, 81.7, 51.9, 3}, {"MM350", 2364, 107, 100, 3}, {"MM325", 2100, 94.7, 93, 5} };
    
    print_mouse_list(mouse_list, LIST_LEN);
    
    return 0;
}


void print_mouse_list(Mouse *list, int length) {
    int i;
    for(i=1; i<length; i++) {
        printf("%s(%d円)\t", (list+i)->name, (list+i)->price);
        printf("：%3.1fcm\t", (list+i)->length);
        printf("%3.1fg\t", (list+i)->weight);
        printf("：ボタン%d個\n", (list+i)->button_num);
    }
}