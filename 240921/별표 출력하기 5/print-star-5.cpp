#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i =n; i >= 1; i --) {
        for (int j = 1; j <= i; j ++) {
            for (int k = 1; k <=i; k ++) {
                cout << "*";
            }
            cout << " ";
        }
        cout << endl;
    }
    return 0;
}