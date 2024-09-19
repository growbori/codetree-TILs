#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int sum_val = 0;
    for (int i = a; i <= b; i ++) {
        sum_val += i;
    }
    cout << sum_val;
    return 0;
}