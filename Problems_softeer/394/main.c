// https://softeer.ai/practice/info.do?idx=1&eid=394

#include <stdio.h>

int main(void) {
    int N, M;
    int members[100000] = {0};
    int isBest[100000] = {0};
    int i;
    int a, b;
    int cnt;
    scanf("%d %d", &N, &M);
    for (i = 0; i < N; i++) {
        scanf("%d", &members[i]);
        isBest[i] = 1;
    }

    for (i = 0; i < M; i++) {
        scanf("%d %d", &a, &b);
        a--;
        b--;
        if (members[a] >= members[b]) {
            isBest[b] = 0;
        }

        if (members[b] >= members[a]) {
            isBest[a] = 0;
        }
    }
    cnt = 0;
    for (i = 0; i < N; i++) {
        if (isBest[i] == 1) {
            cnt++;
        }
    }
    printf("%d", cnt);

    return 0;
}