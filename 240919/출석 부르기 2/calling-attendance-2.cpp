#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    while (true) {
        int i ;
        cin >> i;
        if (i == 1) {
            cout << "John" << endl;
        }
        else if (i == 2) {
            cout << "Tom" << endl;
        }
        else if (i == 3) {
            cout << "Paul" << endl;
        }

        else if (i == 4) {
            cout << "Sam" << endl;
        }
        else {
            cout << "Vacancy" << endl;
            break;
        }
    }
    return 0;
}