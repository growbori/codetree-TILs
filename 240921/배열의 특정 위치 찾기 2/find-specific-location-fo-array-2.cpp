#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    int fir = 0;
    int sec = 0;

    for (int i = 0; i < 10; i ++) {
        cin >> arr[i];
        if (i % 2 == 0) {
            fir += arr[i];
        }
        else {
            sec += arr[i];
        }
    }
    if (fir < sec) {
        cout << sec - fir;
    }
    else {
        cout << fir- sec;
    }
    return 0;
}