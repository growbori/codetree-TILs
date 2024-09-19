#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt = 0;
    while (true) {
        if (n == 1) {
            cout << cnt;
            break;
        }
        else if (n%2 == 0) {
            n = n /2;
            cnt ++;
        }
        else if (n% 2 == 1) {
            n = 3 * n + 1;
            cnt ++;
        }
    }

    return 0;
}