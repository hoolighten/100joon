#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int graph[1001] = { 0, };

int main()
{
    int n, x, h;
    int XMax = 0, HMax = 0;
    int HMax_pos;
    int LeftHeight = 0, RightHeight = 0;
    int dim = 0;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> x >> h;
        graph[x] = h;
        graph[x+1] = max(graph[x], h);
        XMax = max(XMax, x);
        if (h > HMax)
        {
            HMax = h;
            HMax_pos = x; 
        }
    }
    int LeftPos = 0, RightPos = XMax+1;
    graph[HMax_pos+1] = HMax;
    // cout << "leftpart" << endl;
    for(int i = 0; i <= HMax_pos; i++) // 왼쪽에서 시작
    {
        if (LeftHeight < graph[i])
        {
            dim += LeftHeight*(i-LeftPos);
            LeftPos = i;
            LeftHeight = graph[i];
        }
        // cout << "x : " << i << " h : " << LeftHeight << " size : " << dim << endl;
    }
    // cout << "Rightpart" << endl;
    for(int i = XMax+1; i > HMax_pos; i--)
    {
        if (RightHeight < graph[i])
        {
            dim += RightHeight*(RightPos-i);
            RightPos = i;
            RightHeight = graph[i];
        }
        // cout << "x : " << i << " h : " << RightHeight << " size : " << dim << endl;
    }
    cout << dim + HMax;
}
