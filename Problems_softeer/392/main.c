// https://softeer.ai/practice/info.do?idx=1&eid=392

#include <stdio.h>
long Class[1000000][2] = {0};
long Temp[1000000][2] = {0};

void merge_sort(long sIdx, long eIdx) {
    long mIdx;
    long i, j, k;
    if (eIdx - sIdx <= 1) {
        return;
    }
    mIdx = (sIdx + eIdx) / 2;
    merge_sort(sIdx, mIdx);
    merge_sort(mIdx, eIdx);
    i = sIdx;
    j = mIdx;
    k = sIdx;
    while ((i < mIdx) && (j < eIdx)) {
        if (Class[i][1] < Class[j][1]) {
            Temp[k][0] = Class[i][0];
            Temp[k][1] = Class[i][1];
            i++;
        } else if (Class[i][1] > Class[j][1]) {
            Temp[k][0] = Class[j][0];
            Temp[k][1] = Class[j][1];
            j++;
        } else {
            if (Class[i][0] > Class[j][0]) {
                Temp[k][0] = Class[i][0];
                Temp[k][1] = Class[i][1];
                i++;
            } else {
                Temp[k][0] = Class[j][0];
                Temp[k][1] = Class[j][1];
                j++;
            }
        }
        k++;
    }
    while (i < mIdx) {
        Temp[k][0] = Class[i][0];
        Temp[k][1] = Class[i][1];
        i++;
        k++;
    }
    while (j < eIdx) {
        Temp[k][0] = Class[j][0];
        Temp[k][1] = Class[j][1];
        j++;
        k++;
    }
    i = sIdx;
    while (i < eIdx) {
        Class[i][0] = Temp[i][0];
        Class[i][1] = Temp[i][1];
        i++;
    }
}

int main(void) {
    long N;
    long s, e;
    long lastTime;
    long cnt;
    long i;
    scanf("%ld", &N);
    for (i = 0; i < N; i++) {
        scanf("%ld %ld", &s, &e);
        Class[i][0] = s;
        Class[i][1] = e - 1;
    }
    merge_sort(0, N);
    lastTime = 0;
    cnt = 0;
    for (i = 0; i < N; i++) {
        if (Class[i][0] > lastTime) {
            lastTime = Class[i][1];
            cnt++;
        }
    }
    printf("%ld\n", cnt);
    return 0;
}