// https://softeer.ai/practice/info.do?idx=1&eid=409

#include <stdio.h>

int grid[625] = {0};
int res[625] = {0};
int temp[625] = {0};

#define queLimit (1000)
int queue[queLimit] = {0};
int queHeadIdx = -1;
int queTailIdx = 0;
int queSize = 0;

void merge_sort(int sIdx, int eIdx) {
    if (eIdx - sIdx <= 1) {
        return;
    }
    int i, j, k;
    int mIdx;
    mIdx = (sIdx + eIdx) / 2;
    i = sIdx;
    j = mIdx;
    k = sIdx;
    merge_sort(sIdx, mIdx);
    merge_sort(mIdx, eIdx);
    while ((i < mIdx) && (j < eIdx)) {
        if (res[i] < res[j]) {
            temp[k] = res[i];
            i++;
        } else {
            temp[k] = res[j];
            j++;
        }
        k++;
    }

    while (i < mIdx) {
        temp[k] = res[i];
        i++;
        k++;
    }
    while (j < eIdx) {
        temp[k] = res[j];
        j++;
        k++;
    }
    i = sIdx;
    while (i < eIdx) {
        res[i] = temp[i];
        i++;
    }
}

void enqueue(int data) {
    queSize++;
    queHeadIdx++;
    queHeadIdx = queHeadIdx % queLimit;
    queue[queHeadIdx] = data;
}

int dequeue(void) {
    int data;
    if (queSize == 0) {
        return -1;
    } else {
        queSize--;
        data = queue[queTailIdx];
        queTailIdx++;
        queTailIdx = queTailIdx % queLimit;
        return data;
    }
}

void count_island(int startIdx, int N, int cnt) {
    int area = 0;
    int i;
    int x, y;
    enqueue(startIdx);
    grid[startIdx] = 2;
    area++;
    // visited

    while (queSize != 0) {
        i = dequeue();
        x = i % N;
        y = i / N;
        if (y != 0) {
            if (grid[(y - 1) * N + x] == 1) {
                grid[(y - 1) * N + x] = 2;
                enqueue((y - 1) * N + x);
                area++;
            }
        }
        if (y != N - 1) {
            if (grid[(y + 1) * N + x] == 1) {
                grid[(y + 1) * N + x] = 2;
                enqueue((y + 1) * N + x);
                area++;
            }
        }
        if (x != 0) {
            if (grid[y * N + x - 1] == 1) {
                grid[y * N + x - 1] = 2;
                enqueue(y * N + x - 1);
                area++;
            }
        }
        if (x != N - 1) {
            if (grid[y * N + x + 1] == 1) {
                grid[y * N + x + 1] = 2;
                enqueue(y * N + x + 1);
                area++;
            }
        }
    }

    res[cnt] = area;
}

int main(void) {
    int N;
    int cnt;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int i2 = 0; i2 < N; i2++) {
            scanf("%1d", &grid[i * N + i2]);
        }
    }
    cnt = 0;
    for (int i = 0; i < N * N; i++) {
        if (grid[i] == 1) {
            count_island(i, N, cnt);
            cnt++;
        }
    }
    merge_sort(0, cnt);
    printf("%d\n", cnt);
    for (int i = 0; i < cnt; i++) {
        printf("%d\n", res[i]);
    }
    return 0;
}