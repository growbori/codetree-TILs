#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;

    // 1번째 과정
    if (a % 2 == 0) {
        a = a / 2;
    } else {
        a = (a + 1) / 2;
    }

    // 2번째 과정
    if (a % 2 == 0) {
        a = a / 2;
    } else {
        a = (a + 1) / 2;
    }

    // 결과 출력
    cout << a << endl;

    return 0;
}