#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int main(){
    int n, val, ans = 0;

    vector<int> time_v;

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> val; 
        time_v.push_back(val);
    }
    sort(time_v.rbegin(), time_v.rend());
    for(int j = 0; j < n; j++){
        for(int i = j; i < n; i++){
            ans += time_v[i];
        }
    }    
    cout << ans;
}
