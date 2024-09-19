#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, i;
    cin >> a >> b;
    cout << a << " ";
    for (i = a; i < b;) {
        if (i % 2 == 1) {
            i = i * 2;
            if (i <= b) {
                cout << i << " ";
            }
            else {

            }
            
        }
        if (i % 2 == 0) {
            i = i + 3;
            if (i <= b) {
                cout << i << " ";
            }
            else {

            }
            
        }
    }
    return 0;
}