#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, i;
    cin >> a;
    for (i = 1; i <= a; i ++) {
        int b;
        cin >> b;
        if (b % 2 == 1 && b % 3 == 0) {
            cout << b <<endl;
        }
    }
    return 0;
}