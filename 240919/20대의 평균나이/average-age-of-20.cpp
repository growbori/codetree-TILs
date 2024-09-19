#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    float sum = 0;
    int cnt = 0;
    while (true) {
        int a;
        cin >> a;

        if (a / 10 != 2) {
            cout << fixed;
            cout.precision(2);
            cout << sum/cnt << endl;
            break;
        }
        else {
            sum += a;
            cnt += 1;
        }
    }
    return 0;
}