#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a;
    cin >> a;
    int sum_val = 0;
    for (int i = a; i <= 100; i ++) {
        sum_val += i;
    }
    cout << sum_val;
    return 0;
}