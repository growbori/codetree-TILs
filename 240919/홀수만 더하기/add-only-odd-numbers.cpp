#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int sum_val = 0;
    for (int i = 1; i <= n; i ++) {
        int a;
        cin >> a;
        if (a % 2 == 1 && a % 3 == 0) {
            sum_val += a;
        }
    }
    cout << sum_val;
    return 0;
}