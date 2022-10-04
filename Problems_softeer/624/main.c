// https://softeer.ai/practice/info.do?idx=1&eid=624

#include <stdio.h>

int get_seven_seg(int n) {
    int res = 0;
    switch (n) {
        case 0:
            res +=
                (1 << 0) + (1 << 1) + (1 << 2) + (1 << 4) + (1 << 5) + (1 << 6);
            break;
        case 1:
            res += (1 << 2) + (1 << 5);
            break;
        case 2:
            res += (1 << 0) + (1 << 2) + (1 << 3) + (1 << 4) + (1 << 6);
            break;
        case 3:
            res += (1 << 0) + (1 << 2) + (1 << 3) + (1 << 5) + (1 << 6);
            break;
        case 4:
            res += (1 << 1) + (1 << 2) + (1 << 3) + (1 << 5);
            break;
        case 5:
            res += (1 << 0) + (1 << 1) + (1 << 3) + (1 << 5) + (1 << 6);
            break;
        case 6:
            res +=
                (1 << 0) + (1 << 1) + (1 << 3) + (1 << 4) + (1 << 5) + (1 << 6);
            break;
        case 7:
            res += (1 << 0) + (1 << 1) + (1 << 2) + (1 << 5);
            break;
        case 8:
            res += (1 << 0) + (1 << 1) + (1 << 2) + (1 << 3) + (1 << 4) +
                   (1 << 5) + (1 << 6);
            break;
        case 9:
            res +=
                (1 << 0) + (1 << 1) + (1 << 2) + (1 << 3) + (1 << 5) + (1 << 6);
            break;
        default:
            break;
    }
    return res;
}

int get_sevenseg_diff(int amod, int bmod) {
    int cnt, i, ares, bres, res;

    ares = get_seven_seg(amod);
    bres = get_seven_seg(bmod);
    res = ares ^ bres;
    i = 0;
    cnt = 0;
    while (res != 0) {
        if (res % 2) {
            cnt++;
        }
        res = res / 2;
        i++;
    }
    return cnt;
}

int get_push_switch(int a, int b) {
    int cnt, i;
    int amod, bmod;
    cnt = 0;
    i = 0;
    while (i < 5) {
        if (a == 0) {
            amod = 10;
        } else {
            amod = a % 10;
        }
        if (b == 0) {
            bmod = 10;
        } else {
            bmod = b % 10;
        }
        cnt += get_sevenseg_diff(amod, bmod);
        a = a / 10;
        b = b / 10;
        i++;
    }
    return cnt;
}

int main(void) {
    int N, i, a, b;
    scanf("%d", &N);
    int TC[N][2];
    i = 0;
    while (i < N) {
        scanf("%d%d", &a, &b);

        TC[i][0] = a;
        TC[i][1] = b;
        i++;
    }
    i = 0;
    while (i < N) {
        printf("%d\n", get_push_switch(TC[i][0], TC[i][1]));
        i++;
    }

    // printf("%d\n", N);
}
