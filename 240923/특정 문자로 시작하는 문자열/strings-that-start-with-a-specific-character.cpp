#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n; 
    cin >> n;
    string arr[n] = {};
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }
    char x;
    cin >> x;
    int cnt = 0;
    float sum = 0;
    for (int i = 0; i < n; i ++) {
        if (arr[i][0] == x) {
            cnt ++;
            sum += arr[i].length();
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << cnt << " "<< sum/cnt;
    return 0;
}