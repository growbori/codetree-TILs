#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int cnt = 0;
    while (cnt <= 3) {
        int a;
        cin >> a;
        if (a%2 == 1) {
            cnt ++;
            continue;
        }
        else {
            cout << a/2 << endl;
            cnt ++;
        }
    }
    return 0;
}