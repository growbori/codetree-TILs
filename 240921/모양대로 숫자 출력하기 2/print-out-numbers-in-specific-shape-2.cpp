#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt = 2;
    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= n; j ++) {
            if (cnt != 10) {
                cout << cnt;
                cout << " ";
                cnt += 2;
            }
            else {
                cnt = 2;
                cout << cnt;
                cout << " ";
                cnt += 2;
            }
        }
        cout << endl;
    }
    return 0;
}