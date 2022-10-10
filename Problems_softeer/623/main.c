// https://softeer.ai/practice/info.do?idx=1&eid=623
#include <stdio.h>

int main(void) {
    int M, N, K;
    int Secret[100] = {0};
    int Normal[100] = {0};
    int res;
    scanf("%d %d %d", &M, &N, &K);
    for (int i = 0; i < M; i++) {
        scanf("%d", &Secret[i]);
    }
    for (int i = 0; i < N; i++) {
        scanf("%d", &Normal[i]);
    }
    if (N < M) {
        printf("normal\n");
        return 0;
    }
    res = 0;
    for (int i = 0; i < N - M + 1; i++) {
        res = 1;
        for (int i2 = 0; i2 < M; i2++) {
            if (Secret[i2] != Normal[i + i2]) {
                res = 0;
                break;
            }
        }

        if (res == 1) {
            break;
        }
    }
    if (res == 1) {
        printf("secret\n");
    } else {
        printf("normal\n");
    }

    return 0;
}