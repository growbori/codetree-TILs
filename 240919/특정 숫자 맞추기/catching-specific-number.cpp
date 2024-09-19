#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    while (true) {
        int i;
        cin >> i;
        if ( i < 25) {
            cout << "Higher"<< endl;
        }
        else if (i > 25) {
            cout << "Lower" << endl;
        }
        else if (i == 25) {
            cout << "Good" << endl;
            break;
        }
    }
    return 0;
}