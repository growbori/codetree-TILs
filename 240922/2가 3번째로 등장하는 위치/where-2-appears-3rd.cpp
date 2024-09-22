#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;
    int arr[n] = {};
    int count = 0;
    for (int i = 0; i <= n; i ++) {
        cin >> arr[i];
        if (count == 3) {
            cout << i;
            break;
        }
        else {
            if (arr[i] == 2) {
                count ++;
            }
        }
    }
    return 0;
}