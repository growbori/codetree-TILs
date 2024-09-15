#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c, d;
    cin >> a >> b >> c;
    d = min(min(a, b),c);
    cout << d;
    return 0;
}