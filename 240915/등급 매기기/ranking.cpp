#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a;
    cin >> a;
    if (a >= 90) {
        cout << "A";
    }
    else if (a >= 80) {
        cout << "B";
    }
    else if (a >= 70) {
        cout << "C";
    }
    else if (a>= 60) {
        cout << "D";
    }
    else {
        cout << "F";
    }
    return 0;
}