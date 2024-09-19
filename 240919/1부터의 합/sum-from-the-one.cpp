#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;
    int sum = 0;
    for (int i = 1; i <= n ; i ++) {
        if (sum >= n) {
            cout << i-1;
            break;
        }
        else {
            sum += i;
        }
    }
    return 0;
}