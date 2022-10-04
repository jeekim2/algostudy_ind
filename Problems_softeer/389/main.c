// https://softeer.ai/practice/info.do?idx=1&eid=389

#include <stdio.h>

// int student[1000000];
double PSum[100];
// double PSum[1000001];
int main(void) {
    int N, K;
    int i;
    double temp;
    double tempSum;
    int s, e;
    scanf("%d %d", &N, &K);
    PSum[0] = 0;
    tempSum = 0;
    for (i = 0; i < N; i++) {
        scanf(" %lf", &temp);
        tempSum += temp;
        PSum[i + 1] = tempSum;
    }

    for (i = 0; i < K; i++) {
        scanf("%d %d", &s, &e);
        printf("%.2f\n", (PSum[e] - PSum[s - 1]) / (e - s + 1));
    }
    return 0;
}