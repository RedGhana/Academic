// キュー・スタック・リスト、動的メモリ確保
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 4

typedef struct node {
    char name[50];          //氏名
    int age;                //年齢
    struct node *next;      //ポインタ(次のデータを指させる)
} Student;

// Queue
int run_queue();
int enqueue (int *queue, int *head, int *tail, int data, int n);
int dequeue (int *queue, int *head, int *tail, int *data, int n);
int is_full_queue (int *queue, int *head, int *tail, int n);

// Stack
int run_stack();
int push(int *stack, int *sp, int data, int n);
int pop(int *stack, int *sp, int *data);
int is_full_stack(int *stack, int *sp, int n);
void print_stack(int *stack, int sp);

// malloc
int run_malloc();

// list
int run_list();


int main(void) {
    int mode = 0;
    printf("モード選択\n( 1(queue), 2(stack), 3(malloc), 4(list) ): ");
    scanf("%d", &mode);
    
    if(mode == 1) {
        run_queue();
    } else if(mode == 2) {
        run_stack();
    } else if(mode == 3) {
        run_malloc();
    } else if(mode == 4) {
        run_list();
    } else {
        printf("正しいモードを選択してください\n");
    }
    
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
        // スタックのデータが満杯になったかのチェック
        if( !is_full_stack(buf, &sp, N) ) {
            printf("数値入力: ");
            scanf("%d", &data);
            push(buf, &sp, data, N);
            print_stack(buf, sp);
        } else {
            printf("満杯になりました！スタックの中身をすべて吐き出します\n");
            break;
        }
    }
    
    // データの取り出し
    while(1) {
        if( !pop(buf, &sp, &data) ) {
            break;
        }
        printf("数値入力: %d\n", data);
        print_stack(buf, sp);
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

int is_full_stack(int *stack, int *sp, int n) {
    if( *sp < n ) {
        return 0;   //空きあり
    } else {
        return 1;   //満杯
    }
}

void print_stack(int *stack, int sp) {
    printf("スタックの中身... ");
    
    while(sp >= 0) {
        sp--;
        if( sp >= 0 ) {
            printf("%d ", stack[sp]);
        } else {
            // 全データ取り出し完了
            break;
        }
    }
    printf("\n");
}


// 動的メモリ割り当て
int run_malloc() {
    int i, *p, ram_size, data;
    
    printf("動的メモリ領域(データ数): ");
    scanf("%d", &ram_size);
    
    p = (int *) malloc(ram_size * 4);
    
    printf("■ データの入力\n");
    for(i = 0; i < ram_size; i++) {
        printf("No.%d : ", i+1);
        scanf("%d", &data);
        
        p[i] = data;
    }
    
    printf("■ データの表示\n");
    for(i = 0; i < ram_size; i++) {
        printf("No.%d : %d\n", i+1, p[i]);
    }
    
    free(p);
    
    return 0;
}


// リスト
int run_list() {
    Student *head, *now, *p;
    char i_name[64] = {'\0'};
    int i_age = 0, i;
    
    // 最初のデータの作成
    printf("氏名: ");
    scanf("%s", i_name);
    printf("年齢: ");
    scanf("%d", &i_age);
    printf("\n");
    head = (Student *)malloc(sizeof(Student));
    strcpy(head->name, i_name);
    head->age = i_age;
    head->next = NULL;
    now = head;
    
    for(i=0; i<3; i++) {
        // 次のデータの作成
        printf("氏名: ");
        scanf("%s", i_name);
        printf("年齢: ");
        scanf("%d", &i_age);
        printf("\n");
        p = (Student *)malloc(sizeof(Student));
        strcpy(p->name, i_name);
        p->age = i_age;
        p->next = NULL;
        now->next = p;
        now = p;
    }
    
    // suzukiの追加
    p = (Student *)malloc(sizeof(Student));
    strcpy(p->name, "suzuki");
    p->age = 24;
    p->next = NULL;
    now->next = p;
    now = p;
    
    // yamadaの追加 (itouとetouの間の場合)
    p = (Student *)malloc(sizeof(Student));
    strcpy(p->name, "yamada");
    p->age = 19;
    p->next = head->next->next;
    head->next->next = p;
    
    // データの表示
    for(p=head; p!=NULL; p=p->next) {
        printf("アドレス\t: %p\n", p);
        printf("氏名\t\t: %s\n", p->name);
        printf("年齢\t\t: %d\n", p->age);
        printf("next\t\t: %p\n", p->next);
        printf("next_name\t: %s\n\n", p->next->name);
    }
    
    // 全データメモリ開放
    for(p=head; now!=NULL; p=now) {
        now = p->next;
        free(p);
        printf("削除(%p)\n", p);
    }
    free(head);
    free(now);
    
    return 0;
}