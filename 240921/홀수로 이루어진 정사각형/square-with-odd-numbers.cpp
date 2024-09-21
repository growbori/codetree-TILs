#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n; j ++) {
            cout << 10  + 2* j + 2*i +1;
            cout << " ";
        }
        cout << endl;
    }
    return 0;
}