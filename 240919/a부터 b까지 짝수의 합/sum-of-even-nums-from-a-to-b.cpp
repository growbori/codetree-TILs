#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int cnt = 0;
    for (int i= a; i <= b; i ++) {
        if (i % 2 == 0) {
            cnt += i;
        }
    }
    cout << cnt;
    return 0;
}