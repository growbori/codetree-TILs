#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt = 0;
    for (int i = 1; i <= 100; i ++) {
        if (cnt == 2) {
            break;
        }
        else if ((n * i) % 5 == 0) {
            cnt ++;
            cout << n * i << " ";
        }
        else {
            cout << n * i << " ";
        }
    }
    return 0;
}