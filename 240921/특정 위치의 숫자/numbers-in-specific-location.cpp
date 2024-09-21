#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int sum = 0;
    int arr[10];
    for (int i = 0; i < 10; i ++) {
        cin >> arr[i];
    }
    sum += arr[2];
    sum += arr[4];
    sum += arr[9];
    cout << sum;
    return 0;
}