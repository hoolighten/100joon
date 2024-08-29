	#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
 
using namespace std;
 
int N;
int map[17][17];
int dr[3] = {0,1,1};
int dc[3] = {1,0,1};
int answer= 0;
 
bool chk(int r, int c)
{
    if (r < 1 || r > N || c < 1 || c > N || map[r][c] == 1) return false;
    else return true;
}
 
void DFS(int r, int c, int dir){
 
    if(r==N && c==N){
        answer++;
        return;
    }
 
    for(int i = 0; i<3; i++){
        if((dir==0 && i==1) || (dir==1 && i==0)) continue;
        int nr = r + dr[i];
        int nc = c + dc[i];
        if(chk(nr,nc)==false) continue;
        if(i==2 && (map[r+1][c]==1 || map[r][c+1]==1)) continue;    //대각선인데 나머지 칸이 벽이면 
        DFS(nr, nc, i);
    }
}
 
int main()
{
 
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin >> map[i][j];
        }
    }
 
    DFS(1, 2, 0);
    cout << answer;
 
    return 0;
}
