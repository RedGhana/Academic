#include <stdio.h>
#include <string.h>

#define NAME_LEN 64
#define LIST_LEN 100
#define ITEM_COUNT 7
#define TAX 1.1

typedef struct Item {
    char name[NAME_LEN];
    int sell_price;
    int buy_price;
    int num;
} Item;

void print_line_item(Item item);
void print_line_items(Item *list, int num);
int count_out_of_stock_item(Item *list, int num);
int search_item_name(Item *list, int num, Item *hit, char *name);
int calc_item_profit(Item item);
int calc_ctax(int price);

int main(void) {
    Item item_list[LIST_LEN] = { {"USB Memory", 1200, 500, 50}, {"USB Keyboard", 2500, 1300, 20}, {"Wireless Keyboard", 3400, 2000, 0}, {"Display", 23000, 14000, 5}, {"Headphone", 5900, 2900, 10}, {"USB Mouse", 1100, 500, 0}, {"Wireless Mouse", 2400, 1600, 25} };
    Item hit_item = {0};
    char search_name[NAME_LEN];
    int result=0, mode=0;
    
    printf("動作モードを選択してください (0：商品表示　1：在庫確認　2：商品検索　3：利益見込み計算　4：税込み価格計算): ");
    scanf("%d", &mode);
    
    printf("\n");
    switch(mode) {
        case 0:
            printf("------------------商品リスト------------------\n");
            print_line_items(item_list, ITEM_COUNT);
            break;
        case 1:
            if(count_out_of_stock_item(item_list, ITEM_COUNT) == 0) {
                printf("在庫切れの商品はありません\n");
            } else {
                printf("在庫切れの商品が%d点あります\n", count_out_of_stock_item(item_list, ITEM_COUNT) );
                printf("在庫の補充を行ってください\n");
            }
            break;
        case 2:
            printf("探索する商品名を入力: ");
            scanf("%s", search_name);
            result = search_item_name(item_list, ITEM_COUNT, &hit_item, search_name);
            switch (result) {
                case 0:
                    printf("見つかりませんでした\n");
                    break;
                case 1:
                    printf("発見しました！\n");
                    printf("%-20s:%5d円(%5d円)\t:%2d個\n", hit_item.name, hit_item.sell_price, hit_item.buy_price, hit_item.num);
                    break;
                default:
                    printf("エラーが発生。戻り値なし\n");
                    break;
            }
            break;
        case 3:
            printf("利益見込み計算を行う商品名を入力: ");
            scanf("%s", search_name);
            result = search_item_name(item_list, ITEM_COUNT, &hit_item, search_name);
            switch (result) {
                case 0:
                    printf("見つかりませんでした\n");
                    break;
                case 1:
                    printf("「%s」の予想される利益の見込み額は%d円です\n", hit_item.name, calc_item_profit(hit_item));
                    break;
                default:
                    printf("エラーが発生。戻り値なし\n");
                    break;
            }
            break;
        case 4:
            printf("税込み価格計算を行う商品名を入力: ");
            scanf("%s", search_name);
            result = search_item_name(item_list, ITEM_COUNT, &hit_item, search_name);
            switch (result) {
                case 0:
                    printf("見つかりませんでした\n");
                    break;
                case 1:
                    printf("「%s」の税込み価格は%d円です\n", hit_item.name, calc_ctax(hit_item.sell_price));
                    break;
                default:
                    printf("エラーが発生。戻り値なし\n");
                    break;
            }
            break;
        default:
            printf("正しい動作モードを選択してください\n");
            break;
    }
    
    return 0;
}

void print_line_item(Item value) {
    printf("%-20s:%5d円(%5d円)\t:%2d個\n", value.name, value.sell_price, value.buy_price, value.num);
}

void print_line_items(Item *list, int num) {
    int i;
    for(i=0; i<num; i++) {
        print_line_item(list[i]);
    }
}

int count_out_of_stock_item(Item *list, int num) {
    int i, count=0;
    for(i=0; i<num; i++) {
        if(list[i].num == 0) {
            count++;
        }
    }
    return count;
}

int search_item_name(Item *list, int num, Item *hit, char *name) {
    int i;
    for(i=0; i<num; i++) {
        if(strcmp(list[i].name, name) == 0) {
            *hit = list[i];
            return 1;
        }
    }
    return 0;
}

int calc_item_profit(Item item) {
    int profit=0;
    profit = item.sell_price - item.buy_price;
    profit *= item.num;
    
    return profit;
}

int calc_ctax(int price) {
    return (int)((double)price * TAX);
}