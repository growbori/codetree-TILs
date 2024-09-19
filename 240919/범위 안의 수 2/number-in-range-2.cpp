#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    float sum = 0;
    int cnt = 0;
    for (int i = 1; i <= 10; i ++) {
        int a;
        cin >> a;
        if (a >= 0 && a <= 200) {
        sum += a;
        cnt ++ ;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << int(sum) << " " << sum/cnt;
    return 0;
}