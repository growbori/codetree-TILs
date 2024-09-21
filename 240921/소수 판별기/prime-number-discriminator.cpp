#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int c, i;
    cin >> c;
    bool satisfied = true;
    for (i = 2; i < c; i ++) {
        if (c % i == 0) {
            satisfied = false;
        }
    }
    if (satisfied == true) {
        cout << "P";
    }
    else {
        cout << "N";
    }
    return 0;
}