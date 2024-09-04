#include <stdio.h>
#include "03_header.h"

// gcc 03_code_01.c 03_code_02.c 03_code_03.c -o out.o

int main(void) {
    int mode = 0;
    printf("------------------------------\n");
    printf("モード1: 電流計算\n");
    printf("モード2: ASCIIコード表示\n");
    printf("モード3: 温度 - LED 対応表\n");
    printf("モード4: 電験合格確認\n");
    printf("モード5: 商品書き込み(バイナリ)\n");
    printf("モード6: 商品読み込み(バイナリ)\n");
    printf("モード7: 顧客情報書き込み\n");
    printf("モード8: 顧客情報読み込み\n");
    printf("モード9: キュー・デキュー\n");
    printf("モード10: スタック\n");
    printf("モード11: リスト\n");
    printf("モード12: グローバル変数\n");
    printf("------------------------------\n\n");
    printf("動作モード選択: ");
    scanf("%d", &mode);
    printf("\n");
    
    if(mode == 1) {
        calc_current();
    } else if(mode == 2) {
        show_ascii_code();
    } else if(mode == 3) {
        temp_led();
    } else if(mode == 4) {
        score_check();
    } else if(mode == 5) {
        write_item();
    } else if(mode == 6) {
        read_item();
    } else if(mode == 7) {
        write_customer();
    } else if(mode == 8) {
        read_customer();
    } else if(mode == 9) {
        run_queue();
    } else if(mode == 10) {
        run_stack();
    } else if(mode == 11) {
        run_list();
    } else if(mode == 12) {
        add_global();
        printf("GlobalNum: %d\n", GlobalNum);
    } else {
        printf("正しい動作モードを選択してください\n");
    }
    
	return 0;
}