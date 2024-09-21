#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    float sum = 0;
    int cnt = 0;
    float thr = 0;
    for (int i = 0; i < 10; i ++) {
        cin >> arr[i];
        if (i % 2 == 1) {
            sum += arr[i];
        }
        if ((i+1) % 3 == 0) {
            thr += arr[i];
            cnt ++;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << (int)sum << " " << thr/cnt;


    return 0;
}