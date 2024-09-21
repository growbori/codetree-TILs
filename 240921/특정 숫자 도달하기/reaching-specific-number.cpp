#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    float sum = 0;
    int cnt = 0;
    int arr[10];
    for (int i = 0; i < 10; i ++) {
        cin>> arr[i];
        if (arr[i] > 250) {
            break;
        }
        else {
            sum += arr[i];
            cnt ++;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << (int)sum << " " << sum/cnt ;

    return 0;
}