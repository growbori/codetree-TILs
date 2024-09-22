#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int cnt = 0;
    int arr[a] = {};
    for (int i = 0; i < a; i ++) {
        cin >> arr[i];
        if (b == arr[i]) {
            cnt ++;
        }
    }
    cout << cnt;
    return 0;
}