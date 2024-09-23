#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string a, b;
    cin >> a >> b;
    string c, d;
    c = a + b;
    d = b + a;
    if (c == d) {
        cout << "true";
    }
    else {
        cout << "false";
    }
    return 0;
}