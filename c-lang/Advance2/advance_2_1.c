#include <stdio.h>

int main(void) {
    int ia, ib;
    int iaiband, iaibor, iaibxor, ianot, ibnot;
    
    printf("2値を16進数表記で入力：");
    scanf("%x%x", &ia, &ib);
    
    iaiband = ia & ib;  // 論理積AND (bit単位で両方が1の時、1を出力)
                        // 0101 0101 = 0x55 ia
                        // 0000 1111 = 0x0f ib
                        // ---- ----
                        // 0000 0101 = 0x05 ia & ib
                        
    iaibor = ia | ib;  // 論理和OR (bit単位でどちらか一方でも1の時、1を出力)
                        // 0101 0101 = 0x55 ia
                        // 0000 1111 = 0x0f ib
                        // ---- ----
                        // 0101 1111 = 0x5f ia | ib
                        
    iaibxor = ia ^ ib;  // 排他的論理和XOR (bit単位で一致しなければ、1を出力)
                        // 0101 0101 = 0x55 ia
                        // 0000 1111 = 0x0f ib
                        // ---- ----
                        // 0101 1010 = 0x5a ia ^ ib
                        
    ianot = ~ia;        // 否定NOT (bit単位で1,0を反転)
                        // 0101 0101 = 0x55 ia
                        // ---- ----
                        // 1010 1010 = 0xaa ~ia
                        
    ibnot = ~ib;        // 否定NOT (bit単位で1,0を反転)
                        // 0000 1111 = 0x0f ib
                        // ---- ----
                        // 1111 0000 = 0xf0 ~ib
    
    printf(" %04x \t %04x \t %04x \n", ia, ia, ia);
    printf("&%04x \t|%04x \t^%04x \n", ib, ib, ib);
    printf("----- \t----- \t----- \n", ib, ib, ib);
    
    printf(" %04x \t %04x \t %04x \n\n", iaiband, iaibor, iaibxor);
    printf("~ia=%04x \t~ib=%04x \n", ianot, ibnot);
    
    return 0;   
}