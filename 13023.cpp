#include<iostream>
#include<vector>
using namespace std;

vector<int> graph[2001];
bool visited[2001] = { false, };
bool possible = false;

void dfs(int _node, int _cnt);

void dfs(int _node, int _cnt)
{
	if (_cnt == 4) {
		possible = true;
		return;
	}
	visited[_node] = true;
	for (int i = 0; i < graph[_node].size(); i++)
	{
		int new_node = graph[_node][i];
		if (!visited[new_node]) {
			dfs(new_node, _cnt + 1);
			visited[new_node] = false;
		}
	}


}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n, m;
	int f1, f2;
	
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> f1 >> f2;
		graph[f1].push_back(f2);
		graph[f2].push_back(f1);
	}
	for(int i = 0; i < n; i++)
	{
		if (!visited[i]) {
			dfs(i, 0);
			visited[i] = false;
		}
		if (possible) {
			cout << 1 << endl;
			return 0;
		}
	}
	cout << 0 << endl;
	return 0;
}
