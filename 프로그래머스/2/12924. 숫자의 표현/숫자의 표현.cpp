int solution(int n) {
    int ans = 0;

    for (int k = 1; k * (k + 1) / 2 <= n; k++) {
        int x = n - k * (k - 1) / 2;

        if (x % k == 0)
            ans++;
    }

    return ans;
}