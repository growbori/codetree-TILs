#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int arr[n] = {};
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }
    int min_val = INT_MAX;
    for (int i = 0; i < n; i ++) {
        if (min_val > arr[i]) {
            min_val = arr[i];
        }
    }
    int cnt = 0;
    for (int j = 0; j < n; j ++) {
        if (arr[j] == min_val) {
            cnt ++;
        }
    }
    cout << min_val << " " << cnt;
    return 0;
}