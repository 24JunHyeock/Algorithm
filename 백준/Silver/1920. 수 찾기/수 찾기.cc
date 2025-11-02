#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <utility>
#include <unordered_set>


using namespace std;
int main() {
	ios:: sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	unordered_set <int> u;
	for (int i = 0; i < n; i++) {
		int m;
		cin >> m;
		u.insert(m);
	}
	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int h;
		cin >> h;
		if (u.count(h)) {
			cout << 1 << '\n';
		}else cout << 0 << '\n';
	}
	


	return 0;
}