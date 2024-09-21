#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int cnt = 0;
    for (int i = a; i <= b; i ++) {
        int check = 0;
        for (int j = 1; j <= i; j ++) {
            if (i % j == 0) {
                check ++;
            }
        }
        if (check == 3) {
            cnt ++;
        }
    }
    cout << cnt;
    return 0;
}