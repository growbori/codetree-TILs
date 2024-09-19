#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a;
    int cnt = 0;
    for (int i = 1; i <= 5; i ++ ) {
        cin >> a;
        if (a % 2 == 0) {
            cnt ++;
        }
    }
    cout << cnt;
    return 0;
}