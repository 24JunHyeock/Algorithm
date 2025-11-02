#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>




using namespace std;
int main() {
	vector <int> v;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int m;
		cin >> m;
		v.push_back(m);
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < n; i++) {
		cout << v[i] << '\n';
	}


	return 0;
}