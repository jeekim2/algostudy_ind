// https://softeer.ai/practice/info.do?idx=1&eid=584

#include <stdio.h>

int main(void) {
    int N, M;
    int l, v;
    int i, j, k;
    int res, temp;
    int v1[100], v2[100];
    fflush(stdin);
    scanf("%d%d", &N, &M);
    fflush(stdin);
    // int cmd[N][2], ref[M][2];
    i = 0;
    k = 0;
    while (i < N) {
        scanf(" %d%d", &l, &v);
        fflush(stdin);
        j = 0;
        while (j < l) {
            v1[k + j] = v;
            j++;
        }
        k = j + k;
        i++;
    }
    i = 0;
    k = 0;
    while (i < M) {
        scanf(" %d%d", &l, &v);
        fflush(stdin);
        j = 0;
        while (j < l) {
            v2[k + j] = v;
            j++;
        }
        k = j + k;
        i++;
    }
    i = 0;
    res = 0;
    temp = 0;
    while (i < 100) {
        if (v1[i] < v2[i]) {
            temp = v2[i] - v1[i];
        }
        if (res < temp) {
            res = temp;
        }
        i++;
    }
    printf("%d\n", res);
    return 0;
}