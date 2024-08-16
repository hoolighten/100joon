#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, k, idx = 0, cnt = 0;
    int MaxVal = 0;
    int arr[200001];
    int arrIdx[200001] = { 0, };
    cin >> n >> k;
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i]; 
    }
    for(int StIdx = 0; StIdx < n; StIdx++)
    {
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
                arrIdx[arr[StIdx]]--;
                arrIdx[arr[idx]]--;
                cnt--;
                // cout << "초기화" << endl;
                // for(int i = 0; i < n; i++)
                // {
                //     cout << arrIdx[i] << " ";
                // }
                // cout << endl;
                break;
            }
            // for(int i = 0; i < n; i++)
            // {
            //     cout << arrIdx[i] << " ";
            // }
            // cout << endl;
            idx++;
            // cout << "cnt : " << cnt << endl;
            MaxVal = max(MaxVal, cnt);
        }
    }
    cout << MaxVal;
}
