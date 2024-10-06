#include <iostream>
#include <vector>
#include <utility>
#include <queue>
using namespace std;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int max_piece = 0;
int maxX, maxY, type;
vector<vector<int>> acqmap;
queue<pair<int, int>> q;
queue<pair<int, int>> zeroq;
queue<int> wallq;
vector<int> answer;
// 유물 획득 가치를 계산하는 함수
int chk_relic(vector<vector<int>>& graph) {
    bool visited[5][5] = {false}; 
    int totalCnt = 0;

    // Loop through the 3x3 sub-grid centered at (midX, midY)
    for (int x = 0; x < 5; x++) {
        for (int y = 0; y < 5; y++) {
            vector<pair<int, int>> reliceList;
            if (x < 0 || x >= 5 || y < 0 || y >= 5) continue;  // Check bounds
            if (!visited[x][y]) {
                int relicCnt = 1;
                q.push(make_pair(x, y));
                zeroq.push(make_pair(x, y));
                visited[x][y] = true;  // Mark visited

                while (!q.empty()) {
                    pair<int, int> Q_val = q.front();
                    q.pop();
                    int x_val = Q_val.first;
                    int y_val = Q_val.second;

                    for (int i = 0; i < 4; i++) {
                        int nx = x_val + dx[i];
                        int ny = y_val + dy[i];
                        if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && !visited[nx][ny]) {
                            if (graph[x_val][y_val] == graph[nx][ny]) {
                                relicCnt++;
                                q.push(make_pair(nx, ny));
                                zeroq.push(make_pair(nx, ny));
                                visited[nx][ny] = true;
                            }
                        }
                    }
                }

                if (relicCnt >= 3) {
                    totalCnt += relicCnt;
                    while(!zeroq.empty())
                    {
                        pair<int, int> zero = zeroq.front();
                        zeroq.pop();
                        graph[zero.first][zero.second] = 0;
                    }
                }
                while(!zeroq.empty())
                {
                    zeroq.pop();
                }
            }
        }
    }
    return totalCnt;
}

// 오른쪽으로 90도 회전하는 함수
vector<vector<int>> Rotate90(int midX, int midY, const vector<vector<int>>& graph) {
    vector<vector<int>> rotateGraph = graph;
    for (int rX = midX - 1; rX <= midX + 1; rX++) {
        for (int rY = midY - 1; rY <= midY + 1; rY++) {
            rotateGraph[midY + (rY - midY)][midX - (rX - midX)] = graph[rX][rY];
        }
    }
    return rotateGraph;
}

// 오른쪽으로 180도 회전하는 함수
vector<vector<int>> Rotate180(int midX, int midY, const vector<vector<int>>& graph) {
    vector<vector<int>> rotateGraph = graph;
    for (int rX = midX - 1; rX <= midX + 1; rX++) {
        for (int rY = midY - 1; rY <= midY + 1; rY++) {
            rotateGraph[midX - (rX - midX)][midY - (rY - midY)] = graph[rX][rY];
        }
    }
    return rotateGraph;
}

// 오른쪽으로 270도 회전하는 함수
vector<vector<int>> Rotate270(int midX, int midY, const vector<vector<int>>& graph) {
    vector<vector<int>> rotateGraph = graph;
    for (int rX = midX - 1; rX <= midX + 1; rX++) {
        for (int rY = midY - 1; rY <= midY + 1; rY++) {
            rotateGraph[midY - (rY - midY)][midX + (rX - midX)] = graph[rX][rY];
        }
    }
    return rotateGraph;
}

// 주어진 회전 결과를 이용해 최적의 회전 방법을 결정하는 함수
void checkRotation(int midX, int midY, vector<vector<int>>& graph, int rotationType) {
    int piece = chk_relic(graph);
    if (piece > max_piece || (piece == max_piece && rotationType < type)) {
        max_piece = piece;
        maxX = midX;
        maxY = midY;
        type = rotationType;
        acqmap = graph;
    }
}
void FilledWall(vector<vector<int>>& graph)
{
    for(int y = 0; y < 5; y++)
    {
        for(int x = 4; x >= 0; x--)
        {
            if(graph[x][y] == 0)
            {
                int val = wallq.front();
                wallq.pop();
                graph[x][y] = val;
            }
        }
    }

}

int main() {
    int k, m;
    cin >> k >> m;

    vector<vector<int>> acientMap(5, vector<int>(5));
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> acientMap[i][j];
        }
    }
    for (int i = 0; i < m; i++)
    {
        int wall;
        cin >> wall;
        wallq.push(wall);
    }

    // 모든 3x3 서브 그리드에 대해 90도, 180도, 270도 회전 검토
    for(int s = 0; s < k; s++)
    {
        int s_piece = max_piece;
        for (int i = 1; i < 4; i++) {
            for (int j = 1; j < 4; j++) {
                vector<vector<int>> rotated90 = Rotate90(i, j, acientMap);
                checkRotation(i, j, rotated90, 1); // 90도 회전

                vector<vector<int>> rotated180 = Rotate180(i, j, acientMap);
                checkRotation(i, j, rotated180, 2); // 180도 회전

                vector<vector<int>> rotated270 = Rotate270(i, j, acientMap);
                checkRotation(i, j, rotated270, 3); // 270도 회전
            }
        }
        if(max_piece == 0)
        {
            break;
        }

        // 최종 회전 결과 출력
        // cout << "Max Pieces: " << max_piece << ", Center: (" << maxX << ", " << maxY << "), Rotation Type: " << type << endl;

        while(true)
        {
            
            FilledWall(acqmap);
            // for(int a = 0; a < 5; a++)
            // {
            //     for(int b = 0; b < 5; b++)
            //     {
            //         cout << acqmap[a][b] << " ";
            //     }
            //     cout << endl;
            // }
            // cout << endl;
            int cnt = chk_relic(acqmap);
            max_piece+=cnt;
            if (cnt == 0)
            {
                break;
            }
        }
        answer.push_back(max_piece);
        max_piece = 0;
        acientMap = acqmap;
    }
    for(auto ans : answer)
    {
        cout << ans << " ";
    }
    return 0;
}
