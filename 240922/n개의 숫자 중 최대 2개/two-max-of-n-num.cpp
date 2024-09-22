#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;
    int arr[n] = {};
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }
    int max_num = INT_MAX;
    for (int j = 1; j < n; j ++) {
        if (max_num < arr[j]) {
            max_num = arr[j];
        }
    }
    int second = -200000000;
    for (int j = 1; j < n; j ++) {
        if (second < arr[j] && arr[j] != max_num) {
            second = arr[j];
        }
    }
    cout << max_num << " " << second;
    return 0;
}