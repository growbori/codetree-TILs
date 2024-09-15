#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    double a, b;
    cin >> a >> b;
    cout << fixed;
    cout.precision(1);
    cout << (int)(a+b)  << " " << (a+b) / 2 << endl;
    return 0;
}