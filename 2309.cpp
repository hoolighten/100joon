#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int dwarfs[10] = {0, };

int main()
{
    vector<int> real_dwarfs;
    for(int i = 0; i < 9; i++)
    {
        cin >> dwarfs[i];
    }
    int dwarfSum = accumulate(dwarfs, dwarfs+9, 0);

    for(int i = 0; i < 9; i++)
    {
        for(int j = i; j < 9; j++)
        {
            if (dwarfSum-dwarfs[i]-dwarfs[j] == 100)
            {
                for(int k = 0; k < 9; k++)
                {
                    if( k == i || k == j)
                    {
                        continue;
                    }
                    else
                    {
                        real_dwarfs.push_back(dwarfs[k]);
                    }
                }
                sort(real_dwarfs.begin(), real_dwarfs.end());
                for(int i = 0; i < 7; i++)
                {
                    cout << real_dwarfs[i] << endl;
                }
                return 0;
            }
        }
    }

}
