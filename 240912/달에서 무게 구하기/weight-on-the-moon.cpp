#include <iostream>
using namespace std;

int a = 13;

int main() {
    // 여기에 코드를 작성해주세요.
    double b = 0.165000;
    cout << fixed;
    cout.precision(6);
    cout << a << " * " << b << " = " <<  a*b << endl;
    return 0;
}