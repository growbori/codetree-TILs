#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt = 65;
    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= i; j ++) {
            if (cnt == 91) {
                cnt = 65;
                cout << (char)cnt;
                cnt ++;
            }
            else {
                cout << (char)cnt;
                cnt ++;
            }
        }
        cout << endl;
    }
    return 0;
}