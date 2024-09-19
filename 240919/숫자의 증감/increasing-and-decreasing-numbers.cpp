#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, i;
    char c;
    cin >> c >> a;
    if (c == 'A') {
        for (i= 1; i <= a; i ++) {
            cout << i << " ";
        }
    }
    if (c == 'D') {
        for (i = a; i >= 1; i --) {
            cout << i << " ";
        }
    }
    return 0;
}