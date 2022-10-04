// https://softeer.ai/practice/info.do?idx=1&eid=403

#include <stdio.h>

int main(void) {
    int N;
    int i;
    int inASide;
    int tempResA, tempResB, resA, resB;
    scanf("%d", &N);
    int cmd[N][4];
    for (i = 0; i < N - 1; i++) {
        scanf("%d %d %d %d", &cmd[i][0], &cmd[i][1], &cmd[i][2], &cmd[i][3]);
    }
    scanf("%d %d", &cmd[i][0], &cmd[i][1]);
    resA = cmd[0][0];
    resB = cmd[0][1];
    i = 0;
    while (i < N - 1) {
        if (resA + cmd[i + 1][0] > resB + cmd[i + 1][0] + cmd[i][3]) {
            tempResA = resB + cmd[i + 1][0] + cmd[i][3];
        } else {
            tempResA = resA + cmd[i + 1][0];
        }
        if (resB + cmd[i + 1][1] > resA + cmd[i + 1][1] + cmd[i][2]) {
            tempResB = resA + cmd[i + 1][1] + cmd[i][2];
        } else {
            tempResB = resB + cmd[i + 1][1];
        }
        resA = tempResA;
        resB = tempResB;
        i++;
    }
    if (resA > resB) {
        printf("%d\n", resB);
    } else {
        printf("%d\n", resA);
    }

    return 0;
}