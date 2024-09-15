#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c, d, e;
    cin >> a >> b >> c;
    d = min(min(a, b), c);
    e = max(max(a, b), c);
    if ((a != d) && (a != e)) {
        cout << a;
    }
    else if ((b != d) && (b != e)) {
        cout << b;
    }
    else {
        cout << c;
    }
    return 0;
}