#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
	vector<vector<int>> v(9, vector<int>(9));
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> v[i][j];
        }
	}
    int max = -1;
    int row = 0;
    int col = 0;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if( v[i][j] > max) {
                max = v[i][j];
                row = i+1; 
                col = j+1; 
			}
        }
    }
	cout << max << "\n";
	cout << row  << " " << col<< "\n";
    return 0;
}