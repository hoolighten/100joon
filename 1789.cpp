#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    long long s;
    int n = 0;
    cin >> s;
    while(s > 0){
        n++;
        s = s - n;
    }
    if(s < 0){
        n--;
    }
    cout << n;
    return 0;
}
