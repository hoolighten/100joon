#include<iostream>
#include<algorithm>
#include<vector>
#include<limits.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
	int n; cin >> n;
	vector<int>dp(n + 1, 0);
	dp[1] = 1; 
	for (int i = 2; i <= n; i++) {
		int Min = 500001;
		for (int j = 1; j * j <= i; j++) {
			int tmp = i - j * j;
			Min = min(Min, dp[tmp]);
		}
		dp[i] = Min + 1;
	}
	cout << dp[n];
	return 0;
}
