#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 1500001

int dp[MAX] = { 0, };

int main()
{
    int n;
    int val = 0;

    cin >> n;
    vector<pair<int, int>> day;
    day.push_back(make_pair(0, 0));
    for(int i = 0; i < n; i++)
    {
        int T, P;
        cin >> T >> P;
        day.push_back(make_pair(T, P));
    }
    for(int i = 1; i <= n+1; i++)
    {
        val = max(val, dp[i]);
        if(day[i].first+i > n + 1)
        {
            continue;
        }
        dp[i+day[i].first] = max(dp[i+day[i].first], val+day[i].second);
    }
    int answer = val;
    cout << answer;

}
