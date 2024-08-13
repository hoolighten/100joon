#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, k, idx = 0, cnt = 0, max_val = -1;
    int arr[200001];
    int arrIdx[200001] = { 0, };
    cin >> n >> k;
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i]; 
    }
    while(idx < n)
    {
        // cout << "idx : " << idx << endl;
        arrIdx[arr[idx]]++;
        if(arrIdx[arr[idx]] <= k)
        {
            // cout << arr[idx];
            cnt++;
        }
        else
        {
            // cout << "초기화" << endl;
            fill_n(arrIdx, 200001, 0);
            cnt = 1;
        }
        // for(int i = 0; i < n; i++)
        // {
        //     cout << arrIdx[i] << " ";
        // }
        max_val = max(max_val, cnt);
        idx++;
        // cout << "max_val : " << max_val  << " " << "cnt : " << cnt << endl;
    }
    cout << max_val;
}
