#include <stdio.h> 
int main() {
	long long n = 0;
	long long t[6] = { 0 };
	scanf("%lld", &n);
	for (int i = 0; i < 6; i++) {
		scanf("%lld", &t[i]);
	}
	
	long long m = 0;
	long long h = 0;
	scanf("%lld %lld", &m, &h);
	long long cnt = 0;
	
	for (int j = 0; j < 6; j++) {

		if (t[j] == 0)continue;
		cnt += t[j] / m;
		if (t[j] % m != 0)cnt++;
		
	}
	printf("%lld\n", cnt);
	printf("%lld %lld\n", n / h, n % h);
	return 0;
}