#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int cnt;
    for (int i = 1; i <= n; i ++) {
        int check = 0;
        for (int j = 1; j <= i; j ++) {
            if (i % j == 0) {
                check ++;
            }
        }
        if (check == 2) {
            cout << i << " ";
        }
    }

    return 0;
}