#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, i;
    cin >> a;

    for (i = 1; i <= a; i ++) {
        int mul = i % 10;
        if (i % 3 == 0 || mul == 3 || mul == 6 || mul == 9) {
            cout << 0 << " ";
        }
        else if (i / 10 == 3 || i / 10 == 6|| i / 10 == 9) {
            cout << 0 << " ";
        }
        else {
            cout << i << " ";
        }
    }
    return 0;
}