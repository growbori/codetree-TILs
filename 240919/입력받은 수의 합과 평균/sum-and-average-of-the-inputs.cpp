#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    float sum = 0;
    int cnt = 0;
    for (int i = 1; i <= n ; i ++) {
        int a;
        cin >> a;
        sum += a;
        cnt ++;
    }
    cout << fixed;
    cout.precision(1);
    cout << int(sum) << " " << sum/cnt;
    return 0;
}