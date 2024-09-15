#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    double c;
    c = ((10000) * b) / (a * a);
    cout << fixed;
    cout.precision(0);
    if (c >= 25) {
        cout << c << endl << "Obesity" << endl;
    }
    else {
        cout << c << endl;
    }
    return 0;
}