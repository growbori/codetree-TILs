#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 1; i <= n; i ++) {
        int m;
        cin >> m;
        int cnt = 0;
        while (m >= 1) {
            if (m ==1) {
                cout << cnt;
                break;
            }
            else {
                if (m % 2 == 0) {
                    m = m/2;
                    cnt ++;
                }
                else {
                    m = 3 * m + 1;
                    cnt ++;
                }
            }
        }
        cout << endl;
    }
    return 0;
}