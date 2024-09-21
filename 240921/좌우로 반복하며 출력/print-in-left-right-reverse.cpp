#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 1; i <= n; i ++) {
        if (i % 2 == 0) {
            for (int j = n ; j >= 1; j --) {
                cout << j;
            }
        }
        else {
            for (int k = 1; k <= n; k ++) {
                cout << k;
            }
        }
        cout << endl;
    }
    return 0;
}