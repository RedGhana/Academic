// ファイル入出力、キュー・スタック・リスト
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "03_header.h"
#define N 6

typedef struct ITEM {
    char name[64];
    int sell_price;
    int buy_price;
    int stock;
} ITEM;

typedef struct node {
    char name[50];          //氏名
    int age;                //年齢
    struct node *next;      //ポインタ(次のデータを指させる)
} Student;

// Queue
int enqueue (int *queue, int *head, int *tail, int data, int n);
int dequeue (int *queue, int *head, int *tail, int *data, int n);
int is_full_queue (int *queue, int *head, int *tail, int n);

// Stack
int push(int *stack, int *sp, int data, int n);
int pop(int *stack, int *sp, int *data);


int write_item() {
    
    FILE *fp;
    ITEM item;
    
    fp = fopen("item.bin", "wb");
    if(fp == NULL) {
        printf("ファイルをオープンできませんでした\n");
        return 1;
    }
    
    printf("商品の名前: ");
    scanf("%s", item.name);
    printf("販売価格: ");
    scanf("%d", &item.sell_price);
    printf("仕入価格: ");
    scanf("%d", &item.buy_price);
    printf("在庫数: ");
    scanf("%d", &item.stock);
    
    fwrite(&item, sizeof(item), 1, fp);
    printf("item.binに保存しました\n");
    
    fclose(fp);
}

int read_item() {
    FILE *fp;
    ITEM item;
    
    fp = fopen("item.bin", "rb");
    if(fp == NULL) {
        printf("ファイルをオープンできませんでした\n");
        return 1;
    }
    
    
    printf("ファイルに保存された値は以下の通り\n");
    fread(&item, sizeof(item), 1, fp);
    
    printf("商品の名前: %s\n", item.name);
    printf("販売価格: %d\n", item.sell_price);
    printf("仕入価格: %d\n", item.buy_price);
    printf("在庫数: %d\n", item.stock);
    
    fclose(fp);
    
    return 0;
}

int write_customer() {
    
    FILE *fp;
    char name[100], address[100];
    int age;
    
    
    fp = fopen("customer.txt", "a");
    if(fp == NULL) {
        printf("ファイルをオープンできませんでした\n");
        return 1;
    }
    
    printf("名前: ");
    scanf("%s", name);
    printf("年齢: ");
    scanf("%d", &age);
    printf("出身: ");
    scanf("%s", address);
    fprintf(fp, "%s %d %s\n", name, age, address);
    printf("ファイルに書き出しました\n");
    
    fclose(fp);
    
    return 0;
}

int read_customer() {
    FILE *fp;
    char name[100] [100], address[100] [100];
    int age[100];
    int i, num = 0;
    
    fp = fopen("customer.txt", "r");
    if(fp == NULL) {
        printf("ファイルが開けませんでした\n");
        return 1;
    }
    
    while(fscanf(fp, "%s %d %[^\n]\n", name[num], &age[num], address[num]) == 3) {
        num++;
    }
    
    for(i=0; i<num; i++) {
        printf("%-10s\t%2d歳\t出身: %s\t\n", name[i], age[i], address[i]);
    }
    
    fclose(fp);
    
    return 0;
}

int run_queue() {
    int ring_buf[N], head = 0, tail = 0, data;
    
    // データの追加
    while(1) {
        printf("数値を入力: ");
        scanf("%d", &data);
        enqueue(ring_buf, &head, &tail, data, N);
        // リングバッファが満杯になったかのチェック
        if(is_full_queue(ring_buf, &head, &tail, N) == 1) {
            printf("満杯になりました！キューの中身をすべて吐き出します\n");
            break;
        }
    }
    
    // データの取り出し
    while(1) {
        if( !dequeue(ring_buf, &head, &tail, &data, N) ) {
            break;
        }
        printf("%d, ", data);
    }
    printf("\n");
    
    return 0;
}


// エンキュー   初期は head = tail = 0
// 保存できるデータは 要素数-1 個
// 戻り値 成功時:1 失敗時(満杯時):0
int enqueue (int *queue, int *head, int *tail, int data, int n) {
    if( *head != ((*tail + 1) % n) ) {
        queue[*tail % n] = data;
        *tail = (*tail + 1) % n;
        
        return 1;
    } else {
        
        return 0;
    }
}


// デキュー
// 戻り値 成功時:1 失敗時(空時):0
int dequeue (int *queue, int *head, int *tail, int *data, int n) {
    if(*head != *tail) {
        *data = queue[*head];
        *head = (*head + 1) % n;
        
        return 1;
    } else {
        
        return 0;
    }
}


int is_full_queue (int *queue, int *head, int *tail, int n) {
    if( *head != ((*tail + 1) % n) ) {
        // 空きあり
        return 0;
    } else {
        // 満杯
        return 1;
    }
}


// スタック
int run_stack() {
    int buf[N], sp = 0, data;
    
    // データの追加
    while(1) {
        printf("数値入力: ");
        scanf("%d", &data);
        
        // スタックのデータが満杯になったかのチェック
        if( !push(buf, &sp, data, N) ) {
            break;
        }
    }
    
    // データの取り出し
    while(1) {
        if( !pop(buf, &sp, &data) ) {
            break;
        }
        printf("入力数値: %d\n", data);
    }
    
    return 0;
}

// push データの追加
// 戻り値 成功:1 失敗:0
int push(int *stack, int *sp, int data, int n) {
    if( *sp < n ) { //要素を超えていなかったら追加
        stack[*sp] = data;
        (*sp)++;    //次のデータの追加用に要素をインクリメント
        return 1;   //成功
    } else {
        return 0;   //失敗
    }
}

// pop データの取り出し
int pop(int *stack, int *sp, int *data) {
    (*sp)--; //追加時、代入後インクリメントしているため、デクリメントする
    if( *sp >= 0 ) {
        *data = stack[*sp];
        return 1;   //成功
    } else {
        *sp = 0;    //要素番号最低は0
        return 0;   //失敗
    }
}


// リスト
int run_list() {
    Student *head, *now, *p;
    
    // 最初のデータの作成
    head = (Student *)malloc(sizeof(Student));
    strcpy(head->name, "satou");
    head->age = 48;
    head->next = NULL;
    now = head;
    
    // 次のデータの作成
    p = (Student *)malloc(sizeof(Student));
    strcpy(p->name, "itou");
    p->age = 34;
    p->next = NULL;
    now->next = p;
    now = p;
    
    // 次のデータの作成
    p = (Student *)malloc(sizeof(Student));
    strcpy(p->name, "etou");
    p->age = 27;
    p->next = NULL;
    now->next = p;
    now = p;
    
    // 次のデータの作成
    p = (Student *)malloc(sizeof(Student));
    strcpy(p->name, "suzuki");
    p->age = 24;
    p->next = NULL;
    now->next = p;
    now = p;
    
    // 次のデータの作成
    p = (Student *)malloc(sizeof(Student));
    strcpy(p->name, "yamada");
    p->age = 19;
    p->next = NULL;
    now->next = p;
    now = p;
    
    // データの表示
    for(p=head; p!=NULL; p=p->next) {
        printf("アドレス: %p\n", p);
        printf("氏名    : %s\n", p->name);
        printf("年齢    : %d\n", p->age);
        printf("next    : %p\n\n", p->next);
    }
    
    // 全データメモリ開放
    free(p);
    free(head);
    free(now);
    
    return 0;
}