#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    for (int i = 1; i <= a; i ++) {
        for (int j = 1; j <= b; j ++) {
            cout << i * j;
            cout << " "; 
        }
        cout << endl;
    }
    return 0;
}