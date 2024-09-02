#include <vector>
#include <iostream>
using namespace std;
int chkRoad(int graph[][101], int n, int l);




int chkRoad(int graph[][101], int n, int l)
{
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        bool slope[101] = {0,};
        int check = 1;
        for (int j = 1; j < n; j++)
        {
            if (graph[i][j] == graph[i][j - 1]) continue; // 직선길일 경우
            else
            {
                if (graph[i][j] - graph[i][j-1] > 1 || graph[i][j] - graph[i][j-1] < -1) //경사가 너무 높을경우
                {
                    check = 0;
                    break;
                }
                if(graph[i][j] == graph[i][j-1] +1) // 오르막길
                {
                    int cur_height = graph[i][j-1];
                    for(int k = j-1; k > j-l-1; k--)
                    {
                        if (k < 0 || graph[i][k] !=cur_height || slope[k])
                        {
                            check = 0;
                            break;
                        }
                    }
                    if(check==1)
                    {
                        for(int k = j-1; k > j-l-1; k--)
                        {
                            slope[k] = true;
                        }
                    }
                    else break;
                }
                if(graph[i][j] == graph[i][j-1] - 1) // 내리막길
                {
                    int cur_height = graph[i][j];
                    for(int k = j; k < j+l; k++)
                    {
                        if( k >= n || graph[i][k] != cur_height || slope[k])
                        {
                            check = 0;
                            break;
                        }
                    }
                    if(check==1)
                    {
                        for(int k = j; k < j+l; k++)
                        {
                            slope[k] = true;
                        }
                    }
                    else break;
                }
            }
        }
        if(check == 1)
        {
            cnt++;
        }
    }
    return cnt;
   
}

int main()
{
    int r_map[101][101];
    int c_map[101][101];
    int n, l;
    cin >> n >> l;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> r_map[i][j];
            c_map[j][i] = r_map[i][j];
        }
    }
    int answer = 0;
    answer += chkRoad(c_map, n, l);
    answer += chkRoad(r_map, n, l);
    cout << answer;
}
