#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c,d;
    cin >> a >> b >> c >> d;
    if (a > c) {
        cout << "A";
    }
    else if (a == c && b > d) {
        cout << "A";
    }
    else if (a == c && d > b) {
        cout << "B";
    }
    else {
        cout << "B";
    }
    return 0;
}