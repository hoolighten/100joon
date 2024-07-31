#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int k, n;
    long res;
    vector<int> lan;
    cin >> k >> n;
    for(int i = 0; i < k; i++){
        int lan_len;
        cin >> lan_len;
        lan.push_back(lan_len);
    }
    long max = *max_element(lan.begin(), lan.end());
    long s = 1, e = max, mid;
    while(s <= e){
        int cnt = 0;
        mid = (s + e) / 2;
        for(int i = 0; i < k; i++){
            cnt += (int)(lan[i] / mid);
        }
        if(cnt >= n){
            s = mid + 1;
            res = mid;
        }
        else{
            e = mid - 1;
        }
    }
    cout << res << endl;
}
