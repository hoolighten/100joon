// https://www.acmicpc.net/problem/1606
#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

vector<long long> dp(2000001);

int main() {
    long long x, y, start_dog, depth;

    cin >> x >> y;

    // 주어진 좌표 (x, y)에 대한 깊이 계산
    if (x == 0 && y == 0) {
        cout << 1 << endl;
        return 0;
    }

    // 깊이 계산: 원숭이의 인식 방법에 따른 깊이 결정
    depth = max(abs(x), max(abs(y), abs(x + y)));
    // cout << depth << endl;
    // 해당 깊이의 시작 번호 계산
        // DP 배열 초기화
    dp[0] = 1;  // 깊이 0에서의 시작 번호는 1
    for (int i = 1; i < 2000001; i++) {
        dp[i] = dp[i - 1] + 6 * i;  // 이전 깊이의 시작 번호에 6 * i를 더함
    }
    start_dog = dp[depth];

    // 각 방향으로 이동하면서 해당 좌표의 번호 찾기
    long long move_x = depth, move_y = 0;

    // 방향 1: (depth, 0)에서 (depth, -depth)로 이동
    for (int i = 0; i < depth; i++) {
        if (move_x == x && move_y == y) {
            cout << start_dog << endl;
            return 0;
        }
        move_y--;
        start_dog--;
    }

    // 방향 2: (depth, -depth)에서 (0, -depth)로 이동
    for (int i = 0; i < depth; i++) {
        if (move_x == x && move_y == y) {
            cout << start_dog << endl;
            return 0;
        }
        move_x--;
        start_dog--;
    }

    // 방향 3: (0, -depth)에서 (-depth, 0)로 이동
    for (int i = 0; i < depth; i++) {
        if (move_x == x && move_y == y) {
            cout << start_dog << endl;
            return 0;
        }
        move_x--;
        move_y++;
        start_dog--;
    }

    // 방향 4: (-depth, 0)에서 (-depth, depth)로 이동
    for (int i = 0; i < depth; i++) {
        if (move_x == x && move_y == y) {
            cout << start_dog << endl;
            return 0;
        }
        move_y++;
        start_dog--;
    }

    // 방향 5: (-depth, depth)에서 (0, depth)로 이동
    for (int i = 0; i < depth; i++) {
        if (move_x == x && move_y == y) {
            cout << start_dog << endl;
            return 0;
        }
        move_x++;
        start_dog--;
    }

    // 방향 6: (0, depth)에서 (depth, 0)로 이동
    for (int i = 0; i < depth; i++) {
        if (move_x == x && move_y == y) {
            cout << start_dog << endl;
            return 0;
        }
        move_x++;
        move_y--;
        start_dog--;
    }

    return 0;
}
