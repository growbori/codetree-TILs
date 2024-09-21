#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        if (i % 2 == 0) {
            for (int j = i* n+1; j < i* n + n+1 ; j ++) {
                cout << j;
                cout << " ";
            }
        }
        else {
            for (int j = n * (i+1); j > (n* (i+1) - n); j --) {
                cout << j;
                cout << " ";
            }            
        }
        cout << endl;
    }
    return 0;
}