// https://softeer.ai/practice/info.do?idx=1&eid=391

#include <stdio.h>

int main(void) {
    long long mod = 1000000007;
    long long K, P, N;
    long long degP1, degP2, degP3;
    int i;
    long long res;
    scanf("%ld %ld %ld", &K, &P, &N);
    degP1 = (P * P) % mod;
    degP2 = (degP1 * degP1) % mod;
    degP3 = (degP2 * degP2) % mod;
    P = (degP3 * degP1) % mod;
    res = K % mod;
    while (N != 0) {
        if (N % 2) {
            res = (res * P) % mod;
            N = N - 1;
        } else {
            P = (P * P) % mod;
            N = N / 2;
        }
    }
    printf("%ld\n", res);
    return 0;
}
