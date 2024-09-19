#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, i;
    cin >> a;
    for (i = 1; i <= a; i ++ ) {
        if (i % 2 == 0 || i % 3 == 0 ) {
            cout  << 1 << " ";
        }
        else {
            cout << 0 << " ";
        }
    }
    return 0;
}