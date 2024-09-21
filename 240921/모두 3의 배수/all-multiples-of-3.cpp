#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    bool sat = true;
    for (int i = 1; i <= 5; i ++) {
        int c;
        cin >> c;
        if (c % 3 != 0) {
            sat = false;
        }
    }
    if (sat == true) {
        cout << 1;
    }
    else {
        cout << 0;
    }
    return 0;
}