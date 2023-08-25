#include<bits/stdc++.h>


using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N; cin >> N;

	stack<int> st;

	for (int i = 0; i < N; i++)
	{
		string cmd; cin >> cmd;
		if (cmd == "push")
		{
			int num; cin >> num;
			st.push(num);
		}
		else if (cmd == "pop")
		{
			if (st.empty())
			{
				cout << -1 << "\n";
			}
			else
			{
				cout << st.top() << "\n";
				st.pop();
			}
		}
		else if (cmd == "size")
		{
			cout << st.size() << "\n";
		}
		else if (cmd == "empty")
		{
			if (st.empty())
			{
				cout << 1 << "\n";
			}
			else
			{
				cout << 0 << "\n";
			}
		}
		else if (cmd == "top")
		{
			if (st.empty())
			{
				cout << -1 << "\n";
			}
			else
			{
				cout << st.top() << "\n";
			}
		}
	}
}