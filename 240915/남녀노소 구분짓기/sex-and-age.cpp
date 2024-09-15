#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c, d;
    cin >> a >> b;
    if (a == 0) {
        if (b >= 19) {
            cout << "MAN";
        }
        else {
            cout << "BOY";
        }
    }
    else {
        if (b >= 19) {
            cout << "WOMAN";
        }
        else {
            cout << "GIRL";
        }
    }
    return 0;
}