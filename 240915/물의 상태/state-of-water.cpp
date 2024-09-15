#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a;
    cin >> a;
    if (a < 0) {
        cout << "ice" << endl;
    }
    else if (a >= 100) {
        cout << "vapor";
    }
    else {
        cout << "water";
    }
    return 0;
}