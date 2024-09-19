#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt;
    for (int i = 2; i <= n; i ++) {
        if (n % i == 0) {
            cnt ++;
        }
    }
    if (cnt == 0) {
        cout << "N";
    }
    else {
        cout << "C";
    }
    return 0;
}