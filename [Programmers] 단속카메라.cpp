#include <vector>
#include <algorithm>
 
using namespace std;
 
int solution(vector<vector<int>> routes) {
    int answer = 1;
    sort(routes.begin(), routes.end());
    int e = routes[0][1];
    for (auto car_route : routes) {
        if (e < car_route[0]) {
            answer++;
            e = car_route[1];
        }
        if (e >= car_route[1])
        {
            e = car_route[1];
        }
    }
    return answer;
}
