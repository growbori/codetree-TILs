#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
        if (arr[i] % 2 == 0) {
            cout << arr[i] << " ";
        }
    }
    return 0;
}