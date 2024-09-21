#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;

    int total = 0;
    for (int i = 1; i <= n; i ++) {
        int arr[4];
        int sum = 0;
        int cnt = 0;
        for (int i = 0; i < 4; i ++) {
            cin >> arr[i];

            sum += arr[i];
            cnt ++;


        }
        if ((sum / cnt) >= 60) {
            cout << "pass" << endl ;
            total ++;
        }
        else {
            cout << "fail" << endl;
        }
    }
    cout << total;

    return 0;
}