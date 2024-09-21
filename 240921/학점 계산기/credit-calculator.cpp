#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    double sum = 0;
    int cnt = 0;
    double arr[100];
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
        sum += arr[i];
        cnt ++;
    }
    cout<< fixed;
    cout.precision(1);
    cout << sum / cnt << endl;
    if (sum / cnt >= 4.0) {
        cout << "Perfect";
    }
    else if (sum / cnt >= 3.0) {
        cout << "Good";
    }
    else {
        cout << "Poor";
    }
    return 0;
}