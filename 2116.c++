#include <iostream>
#include <vector>
#include <map>
using namespace std;

int BackSide[6] = {5, 3, 4, 1, 2, 0};

int FindMaxSide(vector<int> dice, int _Bottom, int _Top)
{
    int Max;
    for(int num : dice)
    {
        if ( num ==_Bottom || num ==_Top)
        {
            continue;
        }
        Max = max(Max, num);
    }
    return Max;
}

int FindBottomIdx(vector<int> dice, int _Top)
{
    int BottomIdx;
    for(int i = 0; i < 6; i++)
    {
        if (dice[i] == _Top)
        {
            BottomIdx = i;
        }
    }
    return BottomIdx;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n;
    int answer = 0;
    vector<vector<int>> tower(10001, vector<int>(7, 0));
    vector<int> dice;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> tower[i][0] >> tower[i][1] >> tower[i][2] >> tower[i][3] >> tower[i][4] >> tower[i][5]; 
    }
    for(int i = 0; i < 6; i++)
    {
        int Max = 0;
        int Bottom = tower[0][i];
        int Top = tower[0][BackSide[i]];
        Max = FindMaxSide(tower[i], Bottom, Top);
        cout << "next : " << i << endl;
        cout << "Bottom : " << Bottom << " Top : " << Top << " MAXSIDE : " << Max << endl;
        for(int j = 0; j < n; j++)
        {   
            if(j == 0) continue;
            int BottomIdx = FindBottomIdx(tower[j], Top);
            Bottom = tower[j][BottomIdx];
            Top = tower[j][BackSide[BottomIdx]];
            cout << "Bottom : " << Bottom << " Top : " << Top << " MAXSIDE : " << FindMaxSide(tower[j], Bottom, Top) << endl;
            Max += FindMaxSide(tower[j], Bottom, Top);
        }
        answer = max(answer, Max);
    }
    cout << answer;
}
