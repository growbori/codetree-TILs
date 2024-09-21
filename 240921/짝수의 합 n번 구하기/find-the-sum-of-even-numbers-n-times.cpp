#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 1; i <= n; i ++) {
        int a, b;
        cin >> a >> b;
        int sum = 0;
        for (int i = a; i <= b; i ++) {
            if (i % 2 == 0) {
                sum += i;
            }
        }
        cout << sum << endl;
    }

    return 0;
}