#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt = 9;
    for (int i = 1; i <= n ; i ++) {
        for (int j = 1; j <= n; j ++) {
            if (cnt != 0) {
                cout << cnt;
                cnt --;
            }
            else {
                cnt = 9;
                cout << cnt;
                cnt --;
            }
        }
        cout << endl;
    }
    return 0;
}