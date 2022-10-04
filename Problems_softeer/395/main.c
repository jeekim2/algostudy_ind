// https://softeer.ai/practice/inf o.do?idx=1&eid=395

#include <stdio.h>

int main(void) {
    int W, N, M, P;
    int i;
    int JewelWeight[10001] = {
        0,
    };
    int res;
    scanf("%d%d", &W, &N);
    i = 0;
    while (i < N) {
        scanf("%d%d", &M, &P);
        JewelWeight[P] = JewelWeight[P] + M;
        i++;
    }
    i = 10000;
    res = 0;
    while (W > 0) {
        if (JewelWeight[i] != 0) {
            if (W >= JewelWeight[i]) {
                res += i * JewelWeight[i];
                W -= JewelWeight[i];
            } else {
                res += i * W;
                W = 0;
            }
        }
        i--;
    }
    printf("%d", res);

    return 0;
}