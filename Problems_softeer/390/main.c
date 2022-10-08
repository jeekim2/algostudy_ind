// https://softeer.ai/practice/info.do?idx=1&eid=390

#include <stdio.h>

int bs(long* res, int LastIdx, long targetVal) {
    int left, right, mid;
    left = 0;
    right = LastIdx;
    while (right - left > 1) {
        mid = (left + right) / 2;
        if (res[mid] == targetVal) {
            return mid;
        }
        if (res[mid] > targetVal) {
            right = mid;
        } else {
            left = mid;
        }
    }
    mid = (left + right) / 2;
    if (res[mid] == targetVal) {
        return mid;
    }
    if (res[mid] > targetVal) {
        right = mid;
    } else {
        left = mid;
    }
    return right;
}

int main(void) {
    int N;
    long Stones[3000] = {0};
    long res[3000] = {0};
    int LastIdx;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%ld", &Stones[i]);
    }
    res[0] = Stones[0];
    LastIdx = 0;
    for (int i = 1; i < N; i++) {
        if (res[LastIdx] < Stones[i]) {
            res[LastIdx + 1] = Stones[i];
            LastIdx++;
        } else {
            res[bs(res, LastIdx, Stones[i])] = Stones[i];
        }
    }
    printf("%ld\n", LastIdx + 1);
    return 0;
}