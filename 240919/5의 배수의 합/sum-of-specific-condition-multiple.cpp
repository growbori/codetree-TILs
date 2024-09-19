#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int cnt = 0;
    if (a < b) {
        for (int i = a; i <= b; i ++) {
            if (i % 5 == 0) {
                cnt += i;
            }
        }
    cout << cnt;
    }
    else {
        for (int i = b; i <= a; i ++) {
            if (i % 5 == 0) {
                cnt += i;
            }
        }
    cout << cnt;
    }

    return 0;
}