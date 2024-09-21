#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int c;
    cin >> c;
    for (int i = 1; i <= c; i ++) {
        for (int j = 1; j <= c; j ++) {
            cout << "*" ;
        }
        cout << endl;
    }
    return 0;
}