#include<iostream>
#include<vector>

using namespace std;

int main(){
    ios_base::sync_with_stdio(NULL);
    cin.tie(0);
    cout.tie(0);
    vector<int> dp(11, 0);
    int T;
    int n;
    cin >> T;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for (int i = 0; i < T; i++){
        cin >> n;
        if(n <= 3){
            cout << dp[n] << endl;
            continue;
        }
        for(int j = 4; j <= n; j++){
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]; 
        }
        cout << dp[n] << endl;
    }
}

