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

Mouse get_lightest_mouse(Mouse *list, int length);

int main(void) {
    Mouse lightest_mouse={0};
    Mouse mouse_list[LIST_LEN] = { {"MM190", 1182, 115.4, 89.9, 3}, {"MM221", 1399, 99, 77.1, 3}, {"MM235R", 1760, 95, 84, 3}, 
    {"MM187", 1127, 81.7, 51.9, 3}, {"MM350", 2364, 107, 100, 3}, {"MM325", 2100, 94.7, 93, 5} };
    
    lightest_mouse = get_lightest_mouse(mouse_list, LIST_LEN);
    printf("最も軽量なマウスは %s です!\n", lightest_mouse.name);
    
    return 0;
}


Mouse get_lightest_mouse(Mouse *list, int length) {
    int i;
    Mouse result;
    result = *list;
    for(i=0; i<length; i++) {
        if(result.weight > (list+i)->weight) {
            result = *(list+i);
        }
    }
    return result;
}