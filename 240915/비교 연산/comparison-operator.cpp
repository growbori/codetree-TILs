#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c;
    cin >> a >> b;
    c = (a>=b) ? 1:0;
    cout  << c<< endl;
    c = (a>b) ? 1: 0;
    cout  << c<< endl;
    c = (b >= a) ? 1 : 0;
    cout  << c<< endl;
    c = (b>a) ? 1: 0;
    cout  << c<< endl;
    c = (a == b) ? 1: 0;
    cout  << c<< endl;
    c = (a != b) ? 1 : 0;
    cout  << c<< endl;
    return 0;
}